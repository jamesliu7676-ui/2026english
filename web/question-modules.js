window.questionModuleMeta = {
  target: "高中學測英文題型模組",
  sourceBasis: "111-115學年度英文題型統計",
  note: "此模組用於擴充題庫與診斷後練習，不取代正式學測題本。"
};

window.questionModules = [
  {
    id: "reading",
    name: "閱讀測驗",
    examType: "閱讀理解",
    weight: "medium",
    percent: 20.2,
    focus: ["主旨", "細節", "推論", "作者態度"],
    firstGoal: "建立短文題組與限時閱讀"
  },
  {
    id: "discourse",
    name: "篇章結構",
    examType: "篇章與文意",
    weight: "low",
    percent: 3.5,
    focus: ["句子插入", "段落排序", "文意銜接", "轉折線索"],
    firstGoal: "建立上下文線索題"
  },
  {
    id: "cloze",
    name: "文意選填",
    examType: "詞彙與語意",
    weight: "high",
    percent: 71.1,
    focus: ["語境選字", "搭配詞", "轉折詞", "語意一致"],
    firstGoal: "建立語意與篇章線索題"
  },
  {
    id: "fill_blank",
    name: "填字/綜合測驗",
    examType: "詞彙與語意",
    weight: "high",
    percent: 71.1,
    focus: ["詞性", "片語", "文法結構", "語意判斷"],
    firstGoal: "建立單句到短文填空題"
  },
  {
    id: "translation",
    name: "翻譯與寫作",
    examType: "寫作表達",
    weight: "low",
    percent: 5.2,
    focus: ["中翻英", "句型", "連接詞", "段落表達"],
    firstGoal: "建立短句輸出與作文素材題"
  }
];

window.questionModuleExamples = [
  {
    moduleId: "reading",
    level: "A2",
    passage: "AI data centers require large amounts of electricity. Some companies say they will use cleaner energy, but local residents worry about noise, water use, and carbon emissions.",
    question: "What is the main idea of the passage?",
    answer: "AI data centers create both energy opportunities and local concerns.",
    focus: "main idea"
  },
  {
    moduleId: "discourse",
    level: "B1",
    passage: "Many students memorize long vocabulary lists. ____. As a result, they may know a word in isolation but fail to understand it in a passage.",
    question: "Which sentence best fits the blank?",
    answer: "However, they often spend too little time seeing the words in context.",
    focus: "sentence insertion"
  },
  {
    moduleId: "cloze",
    level: "A2",
    passage: "Energy security has become an important issue because supply disruptions can affect prices and daily life.",
    question: "Which word is closest in meaning to disruptions?",
    answer: "interruptions",
    focus: "context meaning"
  },
  {
    moduleId: "fill_blank",
    level: "A2",
    passage: "Students should review mistakes ______ they can avoid repeating them.",
    question: "Choose the best word for the blank.",
    answer: "so that",
    focus: "purpose connector"
  },
  {
    moduleId: "translation",
    level: "B1",
    passage: "",
    question: "Translate into English: 定期複習錯題可以幫助學生避免重複犯錯。",
    answer: "Reviewing mistakes regularly can help students avoid repeating errors.",
    focus: "translation"
  }
];
