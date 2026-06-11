(function () {
  const mobileQuery = window.matchMedia("(max-width: 980px)");
  const body = document.body;
  const quickNav = document.getElementById("mobile-quick-nav");
  const quickButtons = Array.from(document.querySelectorAll(".mobile-quick-btn"));
  const mobileLessonList = document.getElementById("mobile-lesson-list");
  const mobileCurrentLesson = document.getElementById("mobile-current-lesson");
  const upperPanels = document.getElementById("upper-panels");
  const theoryPanel = document.getElementById("theory-panel");
  const codePanel = document.getElementById("code-panel");
  const compilerPanel = document.getElementById("compiler-panel");
  const codeViewer = document.getElementById("code-viewer");

  const sections = {
    lessons: document.getElementById("mobile-lessons-panel"),
    theory: theoryPanel,
    code: codePanel,
    lab: compilerPanel,
  };

  let activeMobileView = "theory";
  let mobileHydrated = false;

  function isMobileLayout() {
    return mobileQuery.matches;
  }

  function setDisplay(node, value) {
    if (node) {
      node.style.display = value;
    }
  }

  function setActiveQuickButton(activeTarget) {
    quickButtons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.mobileTarget === activeTarget);
    });
  }

  function decorateCommentToken(token) {
    if (!token) return;

    token.classList.remove(
      "bc-note",
      "bc-task",
      "bc-question",
      "bc-warning",
      "bc-divider"
    );

    const text = token.textContent.replace(/\s+/g, " ").trim();
    if (!text) return;

    if (/^#+\s*[-=]{4,}/.test(text) || /^#+\s*[=~-]{4,}/.test(text)) {
      token.classList.add("bc-divider");
      return;
    }

    if (/TODO|FIXME|IMPORTANTE|PENDIENTE|TAREA/i.test(text) || /^#\s*!/.test(text)) {
      token.classList.add("bc-task");
      return;
    }

    if (/NOTE|NOTA|IDEA|DEFINICION|DEFINICIÓN/i.test(text) || /^#\s*\*/.test(text)) {
      token.classList.add("bc-note");
      return;
    }

    if (/^\s*#\s*\?/.test(text) || /POR QUE|POR QUÉ|COMO|CÓMO|QUE ES|QUÉ ES/i.test(text)) {
      token.classList.add("bc-question");
      return;
    }

    if (/WARNING|CUIDADO|ATENCION|ATENCIÓN|ERROR|DEPRECADO/i.test(text) || /^#\s*\/\//.test(text)) {
      token.classList.add("bc-warning");
      return;
    }
  }

  function enhanceCodeViewer() {
    if (!codeViewer) return;
    codeViewer.querySelectorAll(".token.comment").forEach(decorateCommentToken);
  }

  function ensureLabReady() {
    if (typeof ensureCompilerLoaded === "function") {
      ensureCompilerLoaded(false);
    }
  }

  function applyMobilePanels(targetKey) {
    if (!isMobileLayout()) return;

    if (targetKey === "lessons") {
      setDisplay(upperPanels, "none");
      setDisplay(theoryPanel, "none");
      setDisplay(codePanel, "none");
      setDisplay(compilerPanel, "none");
    }

    if (targetKey === "theory") {
      setDisplay(upperPanels, "flex");
      setDisplay(theoryPanel, "flex");
      setDisplay(codePanel, "none");
      setDisplay(compilerPanel, "none");
    }

    if (targetKey === "code") {
      setDisplay(upperPanels, "flex");
      setDisplay(theoryPanel, "none");
      setDisplay(codePanel, "flex");
      setDisplay(compilerPanel, "none");
    }

    if (targetKey === "lab") {
      setDisplay(upperPanels, "none");
      setDisplay(theoryPanel, "none");
      setDisplay(codePanel, "none");
      setDisplay(compilerPanel, "flex");
    }

    if (typeof syncPanelLayout === "function") {
      syncPanelLayout();
    }
  }

  function restoreDesktopPanels() {
    if (typeof applyFocusMode === "function") {
      applyFocusMode(
        typeof currentFocusMode === "string" ? currentFocusMode : "todo",
        { persist: false }
      );
      return;
    }

    setDisplay(upperPanels, "");
    setDisplay(theoryPanel, "");
    setDisplay(codePanel, "");
    setDisplay(compilerPanel, "");

    if (typeof syncPanelLayout === "function") {
      syncPanelLayout();
    }
  }

  function setMobileView(targetKey) {
    if (!isMobileLayout() || !sections[targetKey]) return;

    activeMobileView = targetKey;
    body.dataset.mobileView = targetKey;
    setActiveQuickButton(targetKey);
    applyMobilePanels(targetKey);

    if (targetKey === "lab") {
      ensureLabReady();
    }
  }

  function getCurrentLesson() {
    if (
      typeof selectedLessonIndex !== "number" ||
      !Array.isArray(lessons) ||
      selectedLessonIndex < 0 ||
      selectedLessonIndex >= lessons.length
    ) {
      return null;
    }

    return lessons[selectedLessonIndex];
  }

  function syncMobileLessonState() {
    const currentLesson = getCurrentLesson();

    if (mobileCurrentLesson) {
      mobileCurrentLesson.textContent = currentLesson
        ? currentLesson.title
        : "Selecciona una unidad";
    }

    document.querySelectorAll(".mobile-lesson-link").forEach((button, index) => {
      button.classList.toggle("is-active", index === selectedLessonIndex);
    });
  }

  function buildMobileLessonList() {
    if (!mobileLessonList || !Array.isArray(lessons) || mobileHydrated) return;

    const fragment = document.createDocumentFragment();

    lessons.forEach((lesson, index) => {
      const li = document.createElement("li");
      const button = document.createElement("button");

      button.type = "button";
      button.className = "mobile-lesson-link";
      button.innerHTML = [
        "<strong>",
        lesson.title,
        "</strong>",
        "<span>Python",
        lesson.labReady ? " · con lab" : "",
        "</span>"
      ].join("");

      button.addEventListener("click", function () {
        loadLesson(index);
        setMobileView("theory");
      });

      li.appendChild(button);
      fragment.appendChild(li);
    });

    mobileLessonList.appendChild(fragment);
    mobileHydrated = true;
    syncMobileLessonState();
  }

  function hookLessonLoader() {
    if (typeof loadLesson !== "function" || loadLesson.__mobileWrapped) return;

    const originalLoadLesson = loadLesson;

    const wrappedLoadLesson = async function (index) {
      const result = await originalLoadLesson(index);
      syncMobileLessonState();
      enhanceCodeViewer();
      return result;
    };

    wrappedLoadLesson.__mobileWrapped = true;
    loadLesson = wrappedLoadLesson;
  }

  function syncLayoutMode() {
    if (!isMobileLayout()) {
      delete body.dataset.mobileView;
      restoreDesktopPanels();
      return;
    }

    if (!body.dataset.mobileView) {
      setMobileView("theory");
      return;
    }

    setMobileView(activeMobileView);
  }

  if (quickNav) {
    quickNav.addEventListener("click", function (event) {
      const button = event.target.closest(".mobile-quick-btn");
      if (!button) return;
      setMobileView(button.dataset.mobileTarget);
    });
  }

  if (typeof mobileQuery.addEventListener === "function") {
    mobileQuery.addEventListener("change", syncLayoutMode);
  } else if (typeof mobileQuery.addListener === "function") {
    mobileQuery.addListener(syncLayoutMode);
  }

  hookLessonLoader();
  buildMobileLessonList();
  syncMobileLessonState();
  enhanceCodeViewer();
  syncLayoutMode();

  // ── Botón flotante FAB: enviar al Lab desde vista Código ──────────────────
  const fabLab = document.getElementById('mobile-fab-lab');
  if (fabLab) {
    fabLab.addEventListener('click', function () {
      if (typeof sendCurrentCodeToLab === 'function') {
        sendCurrentCodeToLab();
      }
      setMobileView('lab');
    });
  }


})();
