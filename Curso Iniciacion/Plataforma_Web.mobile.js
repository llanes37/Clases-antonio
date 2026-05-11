(function () {
  const mobileQuery = window.matchMedia("(max-width: 920px)");
  const body = document.body;
  const quickNav = document.getElementById("mobile-quick-nav");
  const quickButtons = Array.from(document.querySelectorAll(".mobile-quick-btn"));
  const previewFrame = document.getElementById("preview-frame");
  const btnMobile = document.getElementById("btn-device-mobile");
  const mobileLessonList = document.getElementById("mobile-lesson-list");
  const mobileCurrentLesson = document.getElementById("mobile-current-lesson");

  const sections = {
    lessons: document.getElementById("mobile-lessons-panel"),
    theory: document.getElementById("upper-panel"),
    study: document.getElementById("upper-panel"),
    editor: document.getElementById("editor-panel"),
    preview: document.getElementById("preview-panel"),
  };

  let activeMobileView = "theory";
  let mobileHydrated = false;

  function isMobileLayout() {
    return mobileQuery.matches;
  }

  function setActiveQuickButton(activeTarget) {
    quickButtons.forEach((button) => {
      button.classList.toggle(
        "is-active",
        button.dataset.mobileTarget === activeTarget
      );
    });
  }

  function ensurePreviewMobileMode() {
    if (
      isMobileLayout() &&
      previewFrame &&
      btnMobile &&
      !previewFrame.classList.contains("mobile-mode")
    ) {
      btnMobile.click();
    }
  }

  function setMobileView(targetKey) {
    if (!isMobileLayout() || !sections[targetKey]) return;

    activeMobileView = targetKey;
    body.dataset.mobileView = targetKey;
    setActiveQuickButton(targetKey);

    if (targetKey === "preview") {
      ensurePreviewMobileMode();
    }
  }

  function getCurrentLesson() {
    if (
      typeof currentLessonIndex !== "number" ||
      !Array.isArray(lessons) ||
      currentLessonIndex < 0 ||
      currentLessonIndex >= lessons.length
    ) {
      return null;
    }

    return lessons[currentLessonIndex];
  }

  function syncMobileLessonState() {
    const currentLesson = getCurrentLesson();

    if (mobileCurrentLesson) {
      mobileCurrentLesson.textContent = currentLesson
        ? currentLesson.title
        : "Selecciona una unidad";
    }

    document.querySelectorAll(".mobile-lesson-link").forEach((button, index) => {
      button.classList.toggle("is-active", index === currentLessonIndex);
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
      button.textContent = lesson.title;
      button.addEventListener("click", () => {
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
      return result;
    };

    wrappedLoadLesson.__mobileWrapped = true;
    loadLesson = wrappedLoadLesson;
  }

  function syncLayoutMode() {
    if (!isMobileLayout()) {
      delete body.dataset.mobileView;
      return;
    }

    ensurePreviewMobileMode();

    if (!body.dataset.mobileView) {
      setMobileView("theory");
      return;
    }

    setMobileView(activeMobileView);
  }

  if (quickNav) {
    quickNav.addEventListener("click", (event) => {
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
  syncLayoutMode();
})();
