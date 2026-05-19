# Arabic translations keyed by (case_scenario, English question text prefix match).
# Build script merges these into questions.json.

TOPICS_AR = {
    "Arrays (1D & 2D)": "المصفوفات (أحادية وثنائية الأبعاد)",
    "Binary Search Tree": "شجرة البحث الثنائية",
    "Binary Trees": "الأشجار الثنائية",
    "Bubble Sort": "فرز الفقاعات",
    "Graph Representation": "تمثيل الرسم البياني",
    "Intro to DSA": "مقدمة في هياكل البيانات والخوارزميات",
    "Linked List Implementation": "تنفيذ القائمة المترابطة",
    "Linked Lists": "القوائم المترابطة",
    "Merge Sort": "فرز الدمج",
    "Queue Concepts": "مفاهيم الطابور",
    "Stack": "المكدس",
    "Stack Implementation": "تنفيذ المكدس",
    "Stack Operations": "عمليات المكدس",
}

# Each entry: question_ar, options_ar (a–e)
TRANSLATIONS = {
    "Arrays_case1": {
        "question_ar": "ما هو فهرس العنصر الأول في قائمة بايثون؟",
        "options_ar": {
            "a": "1",
            "b": "-1",
            "c": "0",
            "d": "2",
            "e": "يعتمد على المترجم",
        },
    },
    "Arrays_case2": {
        "question_ar": "تُعرَّف المصفوفة بأنها مجموعة عناصر مخزَّنة في:",
        "options_ar": {
            "a": "مواقع ذاكرة عشوائية",
            "b": "مواقع ذاكرة غير متجاورة",
            "c": "مواقع ذاكرة متجاورة",
            "d": "تخزين خارجي فقط",
            "e": "عناوين ذاكرة افتراضية فقط",
        },
    },
    "Arrays_case3": {
        "question_ar": "إذا كانت مصفوفة ثنائية الأبعاد تحتوي على 5 صفوف و3 أعمدة، فكم عنصرًا فيها؟",
        "options_ar": {"a": "8", "b": "15", "c": "10", "d": "20", "e": "12"},
    },
    "Arrays_case4": {
        "question_ar": "كيف تُخزَّن مصفوفة ثنائية الأبعاد في الذاكرة؟",
        "options_ar": {
            "a": "كتسلسل هرمي شجري",
            "b": "كمواقع تخزين متجاورة حيث تُخزَّن الصفوف واحدًا تلو الآخر",
            "c": "مبعثرة في قطاعات مختلفة من القرص",
            "d": "كقائمة مترابطة غير خطية",
            "e": "في سجلات المعالج فقط",
        },
    },
    "Arrays_case5": {
        "question_ar": "في مصفوفة ثنائية الأبعاد، للوصول إلى العناصر القطرية، أي شرط على فهرس الصف (i) والعمود (j) يُستخدم؟",
        "options_ar": {
            "a": "i < j",
            "b": "i > j",
            "c": "i = j",
            "d": "(i + j) > n",
            "e": "(i + j) < n",
        },
    },
    "BSTImpl_case1": {
        "question_ar": "في شجرة البحث الثنائية، أين يُوضَع قيمة أصغر من العقدة الحالية؟",
        "options_ar": {
            "a": "في الشجرة الفرعية اليمنى",
            "b": "في الشجرة الفرعية اليسرى",
            "c": "في الجذر فقط",
            "d": "في أي موضع فارغ",
            "e": "عشوائيًا في أي مكان",
        },
    },
    "BSTImpl_case2": {
        "question_ar": "في تمثيل العقد المترابطة للشجرة الثنائية، كل عقدة تحتوي عادةً على:",
        "options_ar": {
            "a": "مؤشر إلى العقدة التالية في سلسلة خطية",
            "b": "البيانات ورقم فهرس",
            "c": "البيانات ومؤشر واحد إلى الأب",
            "d": "البيانات ومؤشرات إلى الابن الأيسر والأيمن",
            "e": "البيانات فقط",
        },
    },
    "BinaryTree_case1": {
        "question_ar": "في الشجرة الثنائية، كل عقدة يمكن أن يكون لها على الأكثر:",
        "options_ar": {
            "a": "ابن واحد",
            "b": "ابنان",
            "c": "3 أبناء",
            "d": "4 أبناء",
            "e": "عدد غير محدود من الأبناء",
        },
    },
    "BinaryTree_case2": {
        "question_ar": "ما اسم العقدة الأعلى في الشجرة؟",
        "options_ar": {
            "a": "ورقة",
            "b": "جذر",
            "c": "ابن",
            "d": "حافة",
            "e": "أب",
        },
    },
    "BinaryTree_case3": {
        "question_ar": "ما هي «العقدة الورقية» في الشجرة الثنائية؟",
        "options_ar": {
            "a": "عقدة لها ابن واحد على الأقل",
            "b": "عقدة عند المستوى 0",
            "c": "عقدة لها ابنان بالضبط",
            "d": "عقدة تخزن مؤشرات إلى الجذر",
            "e": "عقدة بلا أبناء",
        },
    },
    "BinaryTree_case4": {
        "question_ar": "أي اجتياز لشجرة BST يُنتج مخرجات مرتبة؟",
        "options_ar": {
            "a": "Preorder",
            "b": "Postorder",
            "c": "In-order",
            "d": "Level-order",
            "e": "عشوائي",
        },
    },
    "BinaryTree_case5": {
        "question_ar": "في شجرة ثنائية كاملة، إذا كان لكل عقدة داخلية ابنان وجميع الأوراق على نفس المستوى، عدد الأوراق يساوي:",
        "options_ar": {
            "a": "نصف العقد الداخلية",
            "b": "ضعف العقد الداخلية",
            "c": "عدد العقد الداخلية",
            "d": "العقد الداخلية + 1",
            "e": "العقد الداخلية − 1",
        },
    },
    "BubbleSort_case1": {
        "question_ar": "ما المبدأ الأساسي لفرز الفقاعات؟",
        "options_ar": {
            "a": "فرق تسد",
            "b": "مبادلة العناصر المتجاورة إذا كان ترتيبهما خاطئًا",
            "c": "إدراج العناصر في قائمة فرعية مرتبة",
            "d": "اختيار أصغر عنصر في كل مرة",
            "e": "استخدام العودية لتقسيم المصفوفات",
        },
    },
    "BubbleSort_case2": {
        "question_ar": "بعد مرور واحد لفرز الفقاعات على القائمة [5, 3, 8, 4]، ما القائمة الناتجة؟",
        "options_ar": {
            "a": "a: [3, 5, 8, 4]",
            "b": "b: [3, 5, 4, 8]",
            "c": "c: [5, 3, 4, 8]",
            "d": "d: [3, 4, 5, 8]",
            "e": "e: [5, 8, 3, 4]",
        },
    },
    "GraphRep_case1": {
        "question_ar": "يتكوَّن الرسم البياني من أي مكوّنين أساسيين؟",
        "options_ar": {
            "a": "عُقد ومصفوفات",
            "b": "رؤوس وحواف",
            "c": "أشجار وكومات",
            "d": "مستويات وأوراق",
            "e": "مؤشرات ومراجع",
        },
    },
    "GraphRep_case2": {
        "question_ar": "ما هي مصفوفة التجاور في تمثيل الرسم البياني؟",
        "options_ar": {
            "a": "قائمة بجميع رؤوس الرسم",
            "b": "مصفوفة ثنائية حيث الخلية (i,j) تخزن معلومات الحافة من الرأس i إلى j",
            "c": "مصفوفة خطية لقيم العُقد",
            "d": "مجموعة أوراق بلا حواف",
            "e": "بنية شجرية تمثل علاقات many-to-many",
        },
    },
    "Intro_DSA_case1_linear": {
        "question_ar": "أيٌّ مما يلي يُعدُّ هيكل بيانات خطيًا؟",
        "options_ar": {
            "a": "شجرة",
            "b": "رسم بياني",
            "c": "طابور",
            "d": "جدول تجزئة",
            "e": "لا شيء مما سبق",
        },
    },
    "Intro_DSA_case1_adt": {
        "question_ar": "ما الميزة الرئيسية لأنواع البيانات المجردة (ADT)؟",
        "options_ar": {
            "a": "تقليل استخدام الذاكرة",
            "b": "إخفاء تفاصيل التنفيذ",
            "c": "تحسين سرعة العتاد",
            "d": "إلغاء العودية",
            "e": "ضمان عمليات O(1)",
        },
    },
    "Intro_DSA_case3": {
        "question_ar": "أي عبارة تميّز بشكل صحيح بين الهياكل الخطية وغير الخطية؟",
        "options_ar": {
            "a": "خطي → طابور، غير خطي → شجرة",
            "b": "خطي → رسم، غير خطي → مصفوفة",
            "c": "خطي → جدول تجزئة، غير خطي → مكدس",
            "d": "خطي → شجرة، غير خطي → طابور",
            "e": "لا شيء مما سبق",
        },
    },
    "LinkedListImpl_case1": {
        "question_ar": "حذف عقدة من بداية القائمة المترابطة يتضمن توجيه الرأس إلى:",
        "options_ar": {
            "a": "NULL",
            "b": "العقدة الأخيرة",
            "c": "العقدة الثانية (head.next)",
            "d": "العقدة الحالية نفسها",
            "e": "عقدة مؤقتة جديدة",
        },
    },
    "LinkedListImpl_case2": {
        "question_ar": "ما غرض عملية الاجتياز (Traversal) في القائمة المترابطة؟",
        "options_ar": {
            "a": "حذف القائمة بالكامل",
            "b": "الوصول إلى كل عنصر في القائمة بالتسلسل",
            "c": "إيجاد العقدة الأخيرة وحذفها",
            "d": "ترتيب القائمة تنازليًا",
            "e": "عكس مؤشرات جميع العُقد",
        },
    },
    "LinkedListImpl_case3": {
        "question_ar": "عند إدراج عقدة في بداية القائمة المترابطة، ما أول خطوة بخصوص المؤشرات؟",
        "options_ar": {
            "a": "جعل الرأس يشير إلى NULL",
            "b": "جعل next للعقدة الجديدة يشير إلى الرأس الحالي",
            "c": "جعل next للعقدة الأخيرة يشير إلى العقدة الجديدة",
            "d": "جعل الرأس يشير إلى العقدة الجديدة فورًا",
            "e": "الاجتياز حتى نهاية القائمة",
        },
    },
    "LinkedList_case1": {
        "question_ar": "كل عنصر في القائمة المترابطة هو كائن منفصل يُسمى:",
        "options_ar": {
            "a": "كتلة",
            "b": "فهرس",
            "c": "عقدة",
            "d": "قطاع",
            "e": "رابط",
        },
    },
    "LinkedList_case2": {
        "question_ar": "إلى ماذا يشير مؤشر next للعقدة الأخيرة في قائمة مفردة الاتجاه؟",
        "options_ar": {
            "a": "الرأس",
            "b": "العقدة الأولى",
            "c": "NULL",
            "d": "نفسها",
            "e": "العقدة السابقة",
        },
    },
    "LinkedList_case3": {
        "question_ar": "كيف تُخصَّص الذاكرة للقائمة المترابطة مقارنة بالمصفوفة؟",
        "options_ar": {
            "a": "المصفوفات عنصرًا بعنصر؛ القوائم ككل مرة واحدة",
            "b": "كلاهما يُخصَّص للبنية كاملة دفعة واحدة",
            "c": "المصفوفات متجاورة؛ القوائم غير متجاورة وتُخصَّص عقدة بعقدة",
            "d": "القوائم لا تستخدم ذاكرة للمؤشرات",
            "e": "المصفوفات أفضل للإدراج والحذف",
        },
    },
    "LinkedList_case4": {
        "question_ar": "أي مؤشر يحدّد العقدة الأولى في القائمة المترابطة؟",
        "options_ar": {
            "a": "Tail",
            "b": "End",
            "c": "Root",
            "d": "Head",
            "e": "Start",
        },
    },
    "LinkedList_case5": {
        "question_ar": "في أي نوع من القوائم المترابطة تشير العقدة الأخيرة إلى الأولى؟",
        "options_ar": {
            "a": "قائمة مزدوجة الاتجاه",
            "b": "قائمة خطية",
            "c": "قائمة مرضية",
            "d": "rear = max_array_size",
            "e": "قائمة ثابتة",
        },
    },
    "MergeSort_case1": {
        "question_ar": "ما أول خطوة في خوارزمية فرز الدمج؟",
        "options_ar": {
            "a": "مبادلة",
            "b": "مقارنة",
            "c": "دمج",
            "d": "تقسيم",
            "e": "مقارنة",
        },
    },
    "MergeSort_case2": {
        "question_ar": "أي خوارزمية تكون عادةً O(n log n) في أسوأ الحالات؟",
        "options_ar": {
            "a": "فرز الفقاعات",
            "b": "فرز الدمج",
            "c": "البحث الخطي",
            "d": "الوصول إلى قمة المكدس",
            "e": "الإدراج",
        },
    },
    "QueueConcepts_case1": {
        "question_ar": "الطابور هيكل بيانات خطي يتبع مبدأ:",
        "options_ar": {
            "a": "آخر داخل أول خارج (LIFO)",
            "b": "أول داخل أول خارج (FIFO)",
            "c": "وصول حسب الأولوية",
            "d": "آخر داخل آخر خارج",
            "e": "وسط داخل أول خارج",
        },
    },
    "QueueConcepts_case2": {
        "question_ar": "أي عملية تزيل وتُرجع العنصر الأمامي في الطابور؟",
        "options_ar": {
            "a": "enqueue()",
            "b": "push()",
            "c": "dequeue()",
            "d": "insert()",
            "e": "delete()",
        },
    },
    "QueueConcepts_case3": {
        "question_ar": "أي مؤشرين يُستخدمان في طابور قائم على مصفوفة؟",
        "options_ar": {
            "a": "Top و Bottom",
            "b": "Start و End",
            "c": "Head و Tail (Front و Rear)",
            "d": "Left و Right",
            "e": "Root و Leaf",
        },
    },
    "QueueConcepts_case4": {
        "question_ar": "ماذا يعني «السعة» (Capacity) في سياق الطابور؟",
        "options_ar": {
            "a": "عدد العناصر الحالي",
            "b": "حجم كل عنصر بيانات",
            "c": "أقصى عدد عناصر يمكن تخزينه",
            "d": "سرعة عملية dequeue",
            "e": "عنوان ذاكرة العقدة الأولى",
        },
    },
    "QueueConcepts_case5": {
        "question_ar": "أي شرط يدل عادةً على أن الطابور الدائري ممتلئ؟",
        "options_ar": {
            "a": "front == -1",
            "b": "rear == -1",
            "c": "(rear + 1) % capacity == front",
            "d": "front == rear في كل الحالات",
            "e": "rear == capacity - 1",
        },
    },
    "Stack_case1_principle": {
        "question_ar": "يعمل هيكل المكدس وفق أي مبدأ؟",
        "options_ar": {
            "a": "FIFO",
            "b": "LIFO",
            "c": "أعلى أولوية أولًا",
            "d": "عشوائي داخل وخارج",
            "e": "من الأسفل للأعلى",
        },
    },
    "Stack_case1_application": {
        "question_ar": "أيٌّ مما يلي تطبيق واقعي للمكدس؟",
        "options_ar": {
            "a": "طابور انتظار التذاكر",
            "b": "مجموعة أوراق أو كومة أطباق",
            "c": "اقتراح أصدقاء في شبكة اجتماعية",
            "d": "مسارات GPS",
            "e": "إدارة مهام الطابعة",
        },
    },
    "Stack_case1_recursion": {
        "question_ar": "أي عملية حاسوبية تعتمد على المكدس لإدارة استدعاءات الدوال وعناوين العودة؟",
        "options_ar": {
            "a": "تقسيم الذاكرة صفحات",
            "b": "العودية في الدوال",
            "c": "فهرسة نظام الملفات",
            "d": "البحث في جدول التجزئة",
            "e": "جدولة الأولويات",
        },
    },
    "StackImpl_case1": {
        "question_ar": "في تنفيذ المكدس، أي عملية تضيف عنصرًا إلى القمة؟",
        "options_ar": {
            "a": "Pop",
            "b": "Push",
            "c": "IsEmpty",
            "d": "Delete",
            "e": "Reset",
        },
    },
    "StackImpl_case2": {
        "question_ar": "عند تنفيذ pop في المكدس، ماذا يجب أن يحدث لمؤشر القمة بعد جلب القيمة؟",
        "options_ar": {
            "a": "stack.top = stack.top + 1",
            "b": "stack.top = stack.top - 1",
            "c": "stack.top = 0",
            "d": "stack.top = size",
            "e": "يبقى المؤشر كما هو",
        },
    },
    "StackImpl_case3": {
        "question_ar": "إذا كان stack.top ≥ stack.size - 1، ما رسالة الخطأ المطلوب طباعتها؟",
        "options_ar": {
            "a": "memory full",
            "b": "stack underflow",
            "c": "stack overflow",
            "d": "array error",
            "e": "index out of bounds",
        },
    },
    "StackOps_case1": {
        "question_ar": "أي دالة تُستخدم للتحقق من أن المكدس فارغ؟",
        "options_ar": {
            "a": "IsFull",
            "b": "Peek",
            "c": "IsEmpty",
            "d": "Pop",
            "e": "Reset",
        },
    },
    "StackOps_case2": {
        "question_ar": "أي عملية تزيل العنصر من قمة المكدس؟",
        "options_ar": {
            "a": "Push",
            "b": "Pop",
            "c": "Peek",
            "d": "Insert",
            "e": "Delete",
        },
    },
    "StackOps_case3": {
        "question_ar": "أي عملية تُرجع قيمة القمة دون إزالتها من المكدس؟",
        "options_ar": {
            "a": "Push",
            "b": "Pop",
            "c": "IsEmpty",
            "d": "Peek",
            "e": "Size",
        },
    },
    "StackOps_case4": {
        "question_ar": "في المكدس، تعيد IsFull القيمة true عندما يكون مؤشر القمة يساوي:",
        "options_ar": {
            "a": "0",
            "b": "-1",
            "c": "capacity - 1",
            "d": "capacity + 1",
            "e": "size / 2",
        },
    },
    "StackOps_case5": {
        "question_ar": "في Push، ما الخطوة مباشرة بعد «التحقق من الامتلاء» (إذا لم يكن ممتلئًا)؟",
        "options_ar": {
            "a": "إضافة البيانات عند القمة الحالية",
            "b": "إنقاص مؤشر القمة",
            "c": "إنهاء البرنامج",
            "d": "زيادة القمة للإشارة إلى الموضع الفارغ التالي",
            "e": "إرجاع خطأ overflow",
        },
    },
}

# Map (case, question substring) -> translation key for duplicate cases
CASE_QUESTION_KEYS = [
    ("Intro_DSA_case1", "linear data structure", "Intro_DSA_case1_linear"),
    ("Intro_DSA_case1", "Abstract Data Types", "Intro_DSA_case1_adt"),
    ("Stack_case1", "operates on which principle", "Stack_case1_principle"),
    ("Stack_case1", "real-world application", "Stack_case1_application"),
    ("Stack_case1", "function calls", "Stack_case1_recursion"),
]


def lookup_translation(case: str, question: str) -> dict | None:
    q_lower = question.lower()
    for c, substr, key in CASE_QUESTION_KEYS:
        if case == c and substr.lower() in q_lower:
            return TRANSLATIONS.get(key)
    return TRANSLATIONS.get(case)
