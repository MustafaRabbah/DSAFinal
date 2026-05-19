const STORAGE_WRONG = "dsa-mcq-wrong-ids";
const STORAGE_LANG = "dsa-mcq-lang-mode";

const LANG = { BOTH: "both", EN: "en", AR: "ar" };

let bank = { questions: [], topics: [], title: "DSA Final MCQs" };
let session = {
  queue: [],
  index: 0,
  correct: 0,
  wrong: 0,
  topicFilter: null,
  difficultyFilter: "all",
};

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

const screens = {
  home: $("#screen-home"),
  quiz: $("#screen-quiz"),
  results: $("#screen-results"),
};

const DIFFICULTY_EN = { easy: "easy", medium: "medium", hard: "hard" };
const DIFFICULTY_AR = { easy: "سهل", medium: "متوسط", hard: "صعب" };

const UI = {
  both: {
    languageHeading: "Language · اللغة",
    languageHint: "Show questions in English, Arabic, or both.",
    quickStart: "Quick start",
    difficulty: "Difficulty",
    byTopic: "By topic",
    practiceAll: "Practice all topics",
    reviewMissed: (n) => `Review missed (${n})`,
    resultsHeading: "Session complete",
    score: "Score",
    correct: "Correct",
    wrong: "Wrong",
    total: "Total",
    tryAgain: "Try again",
    home: "Home",
    exit: "Exit",
    next: "Next",
    seeResults: "See results",
    correctFb: "Correct!",
    wrongFb: "Wrong",
    answerLabel: "Answer",
    noQuestions: "No questions match this filter.",
    questionCount: (c, t) => `${c} questions · ${t} topics`,
    diffAll: "All levels",
    diffEasy: "Easy only",
    diffMedium: "Medium only",
    diffHard: "Hard only",
  },
  en: {
    languageHeading: "Language",
    languageHint: "English only — questions and answers in English.",
    quickStart: "Quick start",
    difficulty: "Difficulty",
    byTopic: "By topic",
    practiceAll: "Practice all topics",
    reviewMissed: (n) => `Review missed (${n})`,
    resultsHeading: "Session complete",
    score: "Score",
    correct: "Correct",
    wrong: "Wrong",
    total: "Total",
    tryAgain: "Try again",
    home: "Home",
    exit: "Exit",
    next: "Next",
    seeResults: "See results",
    correctFb: "Correct!",
    wrongFb: "Wrong",
    answerLabel: "Answer",
    noQuestions: "No questions match this filter.",
    questionCount: (c, t) => `${c} questions · ${t} topics`,
    diffAll: "All levels",
    diffEasy: "Easy only",
    diffMedium: "Medium only",
    diffHard: "Hard only",
  },
  ar: {
    languageHeading: "اللغة",
    languageHint: "العربية فقط — الأسئلة والإجابات بالعربية.",
    quickStart: "بدء سريع",
    difficulty: "الصعوبة",
    byTopic: "حسب الموضوع",
    practiceAll: "تدريب على كل المواضيع",
    reviewMissed: (n) => `مراجعة الأخطاء (${n})`,
    resultsHeading: "انتهت الجلسة",
    score: "النتيجة",
    correct: "صحيح",
    wrong: "خطأ",
    total: "المجموع",
    tryAgain: "حاول مرة أخرى",
    home: "الرئيسية",
    exit: "خروج",
    next: "التالي",
    seeResults: "عرض النتيجة",
    correctFb: "صحيح!",
    wrongFb: "خطأ",
    answerLabel: "الإجابة",
    noQuestions: "لا توجد أسئلة لهذا الاختيار.",
    questionCount: (c, t) => `${c} سؤال · ${t} مواضيع`,
    diffAll: "كل المستويات",
    diffEasy: "سهل فقط",
    diffMedium: "متوسط فقط",
    diffHard: "صعب فقط",
  },
};

function getLangMode() {
  const v = localStorage.getItem(STORAGE_LANG);
  if (v === LANG.EN || v === LANG.AR || v === LANG.BOTH) return v;
  return LANG.BOTH;
}

function showEn() {
  const m = getLangMode();
  return m === LANG.BOTH || m === LANG.EN;
}

function showAr() {
  const m = getLangMode();
  return m === LANG.BOTH || m === LANG.AR;
}

function uiStrings() {
  const m = getLangMode();
  if (m === LANG.AR) return UI.ar;
  if (m === LANG.EN) return UI.en;
  return UI.both;
}

function setLangMode(mode) {
  localStorage.setItem(STORAGE_LANG, mode);
  document.body.dataset.lang = mode;
  document.documentElement.lang = mode === LANG.AR ? "ar" : "en";
  syncLangChips();
  applyStaticLabels();
  applyHeaderLang();
  renderTopicList();
  updateReviewButton();
  if (screens.quiz.classList.contains("active")) renderQuestion();
}

function syncLangChips() {
  const mode = getLangMode();
  $$(".lang-chip").forEach((btn) => {
    btn.classList.toggle("selected", btn.dataset.lang === mode);
    btn.setAttribute("aria-pressed", btn.dataset.lang === mode ? "true" : "false");
  });
}

function bindLangPickers() {
  $$(".lang-chip").forEach((btn) => {
    btn.addEventListener("click", () => {
      setLangMode(btn.dataset.lang);
    });
  });
}

function applyHeaderLang() {
  const mode = getLangMode();
  const titleEn = $("#app-title");
  const titleAr = $("#app-title-ar");
  const subtitle = $("#app-subtitle");

  if (mode === LANG.AR) {
    titleEn.hidden = true;
    titleAr.textContent = bank.title_ar || bank.title || "أسئلة هياكل البيانات";
    titleAr.hidden = false;
    subtitle.textContent = "تدريب للاختبار";
  } else if (mode === LANG.EN) {
    titleEn.hidden = false;
    titleEn.textContent = bank.title || "DSA Final MCQs";
    titleAr.hidden = true;
    subtitle.textContent = "Exam practice";
  } else {
    titleEn.hidden = false;
    titleEn.textContent = bank.title || "DSA Final MCQs";
    titleAr.textContent = bank.title_ar || "";
    titleAr.hidden = !bank.title_ar;
    subtitle.textContent = "Exam practice · English & العربية";
  }
}

function applyStaticLabels() {
  const s = uiStrings();
  const mode = getLangMode();

  $("#label-language-heading").textContent = s.languageHeading;
  $("#label-language-hint").textContent = s.languageHint;
  $("#label-quick-start").textContent = s.quickStart;
  $("#label-difficulty").textContent = s.difficulty;
  $("#label-by-topic").textContent = s.byTopic;
  $("#label-results-heading").textContent = s.resultsHeading;
  $("#label-stat-score").textContent = s.score;
  $("#label-stat-correct").textContent = s.correct;
  $("#label-stat-wrong").textContent = s.wrong;
  $("#label-stat-total").textContent = s.total;
  $("#btn-quiz-all").textContent = s.practiceAll;
  $("#btn-retry").textContent = s.tryAgain;
  $("#btn-home-results").textContent = s.home;
  $("#btn-exit-quiz").textContent = s.exit;

  const sel = $("#filter-difficulty");
  const opts = sel.options;
  opts[0].textContent = s.diffAll;
  opts[1].textContent = s.diffEasy;
  opts[2].textContent = s.diffMedium;
  opts[3].textContent = s.diffHard;

  if (bank.count != null) {
    $("#question-count").textContent = s.questionCount(bank.count, bank.topics?.length || 0);
  }

  document.body.classList.toggle("rtl-ui", mode === LANG.AR);
}

function showScreen(name) {
  Object.entries(screens).forEach(([key, el]) => {
    el.classList.toggle("active", key === name);
  });
  $("#quiz-nav").classList.toggle("hidden", name !== "quiz");
  document.body.style.paddingBottom =
    name === "quiz" ? "calc(88px + env(safe-area-inset-bottom, 0px))" : "";
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function getDifficultyFilter() {
  return $("#filter-difficulty").value;
}

function filterQuestions({ topic = null, difficulty = "all", ids = null } = {}) {
  return bank.questions.filter((q) => {
    if (ids && !ids.includes(q.id)) return false;
    if (topic && q.topic !== topic) return false;
    if (difficulty !== "all" && q.difficulty !== difficulty) return false;
    return true;
  });
}

function loadWrongIds() {
  try {
    const raw = localStorage.getItem(STORAGE_WRONG);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveWrongId(id) {
  const ids = new Set(loadWrongIds());
  ids.add(id);
  localStorage.setItem(STORAGE_WRONG, JSON.stringify([...ids]));
}

function removeWrongId(id) {
  const ids = loadWrongIds().filter((x) => x !== id);
  localStorage.setItem(STORAGE_WRONG, JSON.stringify(ids));
}

function updateReviewButton() {
  const ids = loadWrongIds();
  const btn = $("#btn-review-wrong");
  const available = filterQuestions({ ids }).length;
  const s = uiStrings();
  btn.hidden = available === 0;
  btn.textContent = s.reviewMissed(available);
}

function startQuiz({ topic = null, reviewWrong = false } = {}) {
  const difficulty = getDifficultyFilter();
  let pool;

  if (reviewWrong) {
    pool = filterQuestions({ ids: loadWrongIds(), difficulty });
  } else {
    pool = filterQuestions({ topic, difficulty });
  }

  if (pool.length === 0) {
    alert(uiStrings().noQuestions);
    return;
  }

  session = {
    queue: shuffle(pool),
    index: 0,
    correct: 0,
    wrong: 0,
    topicFilter: topic,
    difficultyFilter: difficulty,
  };

  showScreen("quiz");
  renderQuestion();
}

function renderQuestion() {
  const q = session.queue[session.index];
  const total = session.queue.length;
  const n = session.index + 1;
  const s = uiStrings();

  $("#progress-fill").style.width = `${(n / total) * 100}%`;

  const topicEl = $("#quiz-topic");
  topicEl.innerHTML = "";
  if (showEn()) {
    const enSpan = document.createElement("span");
    enSpan.textContent = q.topic;
    topicEl.appendChild(enSpan);
  }
  if (showAr() && q.topic_ar) {
    const arSpan = document.createElement("span");
    arSpan.className = "topic-ar lang-ar";
    arSpan.dir = "rtl";
    arSpan.textContent = q.topic_ar;
    topicEl.appendChild(arSpan);
  }

  $("#quiz-counter").textContent = `${n} / ${total}`;

  const badge = $("#quiz-difficulty");
  const enD = DIFFICULTY_EN[q.difficulty] || q.difficulty;
  const arD = DIFFICULTY_AR[q.difficulty] || "";
  if (showEn() && showAr()) {
    badge.textContent = `${enD} · ${arD}`;
  } else if (showAr()) {
    badge.textContent = arD;
  } else {
    badge.textContent = enD;
  }
  badge.className = `badge badge-${q.difficulty}`;

  const qEn = $("#question-text-en");
  const qAr = $("#question-text-ar");

  if (showEn()) {
    qEn.textContent = q.question;
    qEn.hidden = false;
  } else {
    qEn.textContent = "";
    qEn.hidden = true;
  }

  if (showAr() && q.question_ar) {
    qAr.textContent = q.question_ar;
    qAr.hidden = false;
  } else {
    qAr.textContent = "";
    qAr.hidden = true;
  }

  const card = qEn.closest(".card");
  card.classList.toggle("single-lang", !showEn() || !showAr());

  const optionsEl = $("#options");
  optionsEl.innerHTML = "";

  const letters = ["a", "b", "c", "d", "e"];
  letters.forEach((letter) => {
    const textEn = q.options[letter];
    const textAr = q.options_ar?.[letter];
    const hasEn = textEn && String(textEn).trim();
    const hasAr = textAr && String(textAr).trim();
    if (!hasEn && !hasAr) return;
    if (showEn() && !hasEn) return;
    if (showAr() && !hasAr && !showEn()) return;
    if (!showEn() && !hasAr) return;

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "option";
    btn.dataset.letter = letter;

    let labelHtml = "";
    if (showEn() && hasEn) {
      labelHtml += `<span class="label-en">${escapeHtml(textEn)}</span>`;
    }
    if (showAr() && hasAr) {
      labelHtml += `<span class="label-ar lang-ar" dir="rtl">${escapeHtml(textAr)}</span>`;
    }

    btn.innerHTML = `<span class="letter">${letter.toUpperCase()}</span><span class="label-wrap">${labelHtml}</span>`;
    btn.addEventListener("click", () => onAnswer(letter, btn));
    optionsEl.appendChild(btn);
  });

  const feedback = $("#feedback");
  feedback.className = "feedback";
  feedback.innerHTML = "";

  $("#btn-next").disabled = true;
  $("#btn-next").textContent =
    session.index === total - 1 ? s.seeResults : s.next;
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function getAnswerText(q) {
  if (showEn()) return q.options[q.answer];
  return q.options_ar?.[q.answer] || q.options[q.answer];
}

function onAnswer(letter, btn) {
  const q = session.queue[session.index];
  if (document.querySelector(".option:disabled")) return;

  const s = uiStrings();
  const correct = letter === q.answer;

  document.querySelectorAll(".option").forEach((el) => {
    el.disabled = true;
    const L = el.dataset.letter;
    if (L === q.answer) el.classList.add("reveal-correct", "correct");
    else if (L === letter && !correct) el.classList.add("wrong");
  });

  const feedback = $("#feedback");
  feedback.classList.add("show", correct ? "ok" : "bad");

  const ansText = getAnswerText(q);
  const ansEn = q.options[q.answer];
  const ansAr = q.options_ar?.[q.answer] || "";

  if (correct) {
    if (showEn() && showAr()) {
      feedback.innerHTML = `<strong>${s.correctFb}</strong> · <span dir="rtl" class="lang-ar">${UI.ar.correctFb}</span>`;
    } else {
      feedback.innerHTML = `<strong>${s.correctFb}</strong>`;
    }
    removeWrongId(q.id);
    session.correct += 1;
  } else {
    session.wrong += 1;
    saveWrongId(q.id);
    let html = `<strong>${s.wrongFb}</strong><br>${s.answerLabel}: <strong>${q.answer.toUpperCase()}</strong> — ${escapeHtml(ansText)}`;
    if (showEn() && showAr() && ansAr && ansEn !== ansAr) {
      html += `<br><span class="lang-ar" dir="rtl">${escapeHtml(ansAr)}</span>`;
    }
    feedback.innerHTML = html;
  }

  updateReviewButton();
  $("#btn-next").disabled = false;
}

function nextQuestion() {
  if (session.index < session.queue.length - 1) {
    session.index += 1;
    renderQuestion();
  } else {
    showResults();
  }
}

function showResults() {
  const total = session.queue.length;
  const pct = total ? Math.round((session.correct / total) * 100) : 0;

  $("#stat-score").textContent = `${pct}%`;
  $("#stat-correct").textContent = String(session.correct);
  $("#stat-wrong").textContent = String(session.wrong);
  $("#stat-total").textContent = String(total);

  showScreen("results");
}

function renderTopicList() {
  const counts = {};
  bank.questions.forEach((q) => {
    counts[q.topic] = (counts[q.topic] || 0) + 1;
  });

  const ul = $("#topic-list");
  ul.innerHTML = "";

  bank.topics.forEach((topic) => {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.type = "button";

    const ar = bank.topics_ar?.[topic] || "";
    let labelHtml = "";
    if (showEn()) labelHtml += `<span class="topic-en">${escapeHtml(topic)}</span>`;
    if (showAr() && ar) {
      labelHtml += `<span class="topic-ar lang-ar" dir="rtl">${escapeHtml(ar)}</span>`;
    }
    if (!labelHtml) labelHtml = `<span>${escapeHtml(topic)}</span>`;

    btn.innerHTML = `<span>${labelHtml}</span><span class="topic-count">${counts[topic] || 0}</span>`;
    btn.addEventListener("click", () => startQuiz({ topic }));
    li.appendChild(btn);
    ul.appendChild(li);
  });
}

function goHome() {
  showScreen("home");
  updateReviewButton();
}

async function init() {
  bindLangPickers();

  try {
    const res = await fetch("questions.json");
    if (!res.ok) throw new Error(res.statusText);
    bank = await res.json();
  } catch (e) {
    $("#question-count").textContent =
      "Could not load questions. Open via GitHub Pages or a local server.";
    console.error(e);
    return;
  }

  setLangMode(getLangMode());

  $("#btn-quiz-all").addEventListener("click", () => startQuiz());
  $("#btn-review-wrong").addEventListener("click", () =>
    startQuiz({ reviewWrong: true })
  );
  $("#btn-next").addEventListener("click", nextQuestion);
  $("#btn-exit-quiz").addEventListener("click", goHome);
  $("#btn-retry").addEventListener("click", () => {
    if (session.topicFilter) startQuiz({ topic: session.topicFilter });
    else startQuiz();
  });
  $("#btn-home-results").addEventListener("click", goHome);
}

init();
