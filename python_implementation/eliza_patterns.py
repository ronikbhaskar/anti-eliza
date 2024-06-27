
ELIZA_PATTERNS = [
    (r'I feel (.*)',
        ["Why do you feel {0}?", "How long have you felt {0}?", "What do you think has contributed to you feeling {0}?"]),
    (r'What should I do (.*)',
        ["What do you think would happen if you {0}?", "Have you considered your options regarding {0}?", "How do you usually handle situations like {0}?"]),
    (r'How do I (.*)',
        ["Why do you want to know how to {0}?", "What do you think would be the best way to {0}?", "Have you sought advice from others about how to {0}?"]),
    (r'Why do I (.*)',
        ["What makes you think you {0}?", "How do you feel about {0}?", "Have you noticed any patterns or triggers related to {0}?"]),
    (r"(I\'?m|I am) worried (about|for) (.*)",
        ["What specifically are you worried about regarding {2}?", "How does this worry affect your daily life?", "Have you talked to anyone else about your worries regarding {2}?"]),
    (r'What\'?s wrong with me(.*)',
        ["Why do you think something is wrong with you?", "What symptoms or feelings are you experiencing?", "Have you considered seeking professional advice?"]),
    (r'Can you help me (.*)',
        ["I'm here to listen and provide support. What do you need help with regarding {0}?", "What kind of help are you looking for regarding {0}?", "Have you thought about how you can help yourself with {0}?"]),
    (r'How can I (.*)',
        ["What do you think would be the first step to {0}?", "Have you explored different ways to {0}?", "Is there someone you trust who could advise you on how to {0}?"]),
    (r'When should I (.*)',
        ["What do you think would be the right time to {0}?", "Have you considered the consequences of {0}?", "How do you usually decide when to {0}?"]),
    (r'I don\'?t know (.*)',
        ["It's okay not to know. What would help you figure it out?", "What do you think is preventing you from knowing {0}?", "Have you considered exploring different perspectives on {0}?"]),
    (r"(I\'?m|I am) not sure (.*)",
        ["Why are you uncertain about {1}?", "What makes you unsure about {1}?", "How do you feel about your uncertainty regarding {1}?"]),
    (r"(I\'?d|I would) like to (.*)",
        ["Why would you like to {1}?", "What would it mean to you if you could {1}?", "What's stopping you from {1}?"]),
    (r'Can you explain (.*)',
        ["Why do you want me to explain {0}?", "What part of {0} do you find confusing?", "How would an explanation of {0} help you?"]),
    (r"(I\'?m|I am) afraid (.*)",
        ["What are you afraid of regarding {1}?", "How does your fear of {1} affect you?", "What do you think you could do to overcome your fear of {1}?"]),
    (r"(I\'?m|I am) happy (.*)",
        ["What's making you feel happy about {1}?", "How long have you been happy about {1}?", "How do you express your happiness about {1}?"]),
    (r"(I\'?m|I am) sad (.*)",
        ["I'm sorry to hear that you're sad about {1}.", "What do you think is causing your sadness about {1}?", "How do you usually cope with sadness about {1}?"]),
    (r'What do you think about (.*)',
        ["Why are you asking me about {0}?", "What's your opinion on {0}?", "How does {0} make you feel?"]),
    (r'Tell me more about yourself',
        ["Why do you want to know more about me?", "How does knowing more about me help you?", "What would you like to know about me?"]),
    (r'How do you feel about (.*)',
        ["How do you feel about {0}?", "What emotions does {0} evoke for you?", "Why do you want to know how I feel about {0}?"]),
    (r'Let\'s talk about (.*)',
        ["Sure, let's discuss {0}. What specifically about {0} interests you?", "Why do you want to talk about {0}?", "How does {0} relate to your current thoughts?"]),
    (r"(I'?ve|I have) never (.*)", 
        ["Why have you never {1}?", "Would you like to {1}?", "What would it take for you to {1}?"]),
    (r'Are you sure (.*)', 
        ["Do you doubt that {0}?", "What makes you uncertain about {0}?", "Why are you questioning {0}?"]),
    (r'It seems like (.*)', 
        ["Why does it seem like {0}?", "What makes you think {0}?", "How do you feel about {0}?"]),
    (r'I often (.*)', 
        ["How often do you {0}?", "Why do you {0} so often?", "What does {0} bring to your life?"]),
    (r'Sometimes I (.*)', 
        ["When do you usually {0}?", "Why do you sometimes {0}?", "How does it feel when you {0}?"]),
    (r'What if (.*)', 
        ["What do you think would happen if {0}?", "How would you feel if {0}?", "Why do you ask what if {0}?"]),
    (r'I wonder if (.*)', 
        ["What makes you wonder if {0}?", "Why do you wonder if {0}?", "How does wondering about {0} make you feel?"]),
    (r"(I'?ve|I have) heard that (.*)", 
        ["Where did you hear that {0}?", "What do you think about {0}?", "How do you feel about hearing that {0}?"]),
    (r'My favorite (.*)', 
        ["Why is {0} your favorite?", "What do you like about {0}?", "How does {0} being your favorite make you feel?"]),
    (r'I remember (.*)', 
        ["What do you remember about {0}?", "Why do you remember {0}?", "How does remembering {0} make you feel?"]),
    (r'Tell me about (.*)',
        ["What do you want to know about {0}?", "Why are you interested in {0}?", "What does {0} mean to you?"]),
    (r'I feel (.*) about (.*)',
        ["Why do you feel {0} about {1}?", "What led you to feel {0} about {1}?", "How long have you felt {0} about {1}?"]),
    (r'(.*) makes me (.*)',
        ["Why does {0} make you {1}?", "How often does {0} make you {1}?", "What is it about {0} that makes you {1}?"]),
    (r'I wish (.*)',
        ["Why do you wish {0}?", "How would you feel if {0}?", "What would change if you got your wish about {0}?"]),
    (r'People (.*)',
        ["What people are you referring to?", "How do these people make you feel?", "Why do you think people {0}?"]),
    (r'(.*) (annoy|bother)s? me',
        ["Why does {0} annoy you?", "How do you usually deal with {0}?", "What could you do to feel less annoyed by {0}?"]),
    (r"(I'?ve|I have) been (.*)",
        ["How long have you been {1}?", "What has led you to be {1}?", "How do you feel about being {1}?"]),
    (r'I wonder (.*)',
        ["What makes you wonder {0}?", "Why is {0} on your mind?", "What do you think about when you wonder {0}?"]),
    (r'Can we talk about (.*)',
        ["Sure, what about {0}?", "Why do you want to talk about {0}?", "What specifically about {0} interests you?"]),
    (r'How come (.*)',
        ["Why do you think {0}?", "What makes you curious about {0}?", "How do you feel about {0}?"]),
    (r'I need (.*)',
        ["Why do you need {0}?", "Would it really help you to get {0}?", "Are you sure you need {0}?"]),
    (r'Why don\'?t you (.*)',
        ["Do you really think I don't {0}?", "Perhaps eventually I will {0}.", "Do you really want me to {0}?"]),
    (r'Why can\'?t I (.*)',
        ["Do you think you should be able to {0}?", "If you could {0}, what would you do?", "I don't know -- why can't you {0}?", "Have you really tried?"]),
    (r'I can\'?t (.*)',
        ["How do you know you can't {0}?", "Perhaps you could {0} if you tried.", "What would it take for you to {0}?"]),
    (r'I am (.*)',
        ["Did you come to me because you are {0}?", "How long have you been {0}?", "How do you feel about being {0}?"]),
    (r'I\'?m (.*)',
        ["How does being {0} make you feel?", "Do you enjoy being {0}?", "Why do you tell me you're {0}?", "Why do you think you're {0}?"]),
    (r'Are you (.*)',
        ["Why does it matter whether I am {0}?", "Would you prefer it if I were not {0}?", "Perhaps you believe I am {0}.", "I may be {0} -- what do you think?"]),
    (r'What (.*)',
        ["Why do you ask?", "How would an answer to that help you?", "What do you think?"]),
    (r'How (.*)',
        ["How do you suppose?", "Perhaps you can answer your own question.", "What is it you're really asking?"]),
    (r'(Because|Since) (.*)',
        ["Is that the real reason?", "What other reasons come to mind?", "Does that reason apply to anything else?", "If {1}, what else must be true?"]),
    (r'(.*) (sorry|apologize) (.*)',
        ["There are many times when no apology is needed.", "What feelings do you have when you apologize?"]),
    (r'(Hello|Hi |Hey |Howdy|Greetings)(.*)',
        ["Hello... I'm glad you could drop by today.", "Hi there... how are you today?", "Hello, how are you feeling today?"]),
    (r'I think (.*)',
        ["Do you doubt {0}?", "Do you really think so?", "But you're not sure {0}?"]),
    (r'(.*) friend (.*)',
        ["Tell me more about your friends.", "When you think of a friend, what comes to mind?", "Why don't you tell me about a childhood friend?"]),
    (r'(Yes|Yeah|Yep)',
        ["You seem quite sure.", "OK, but can you elaborate a bit?"]),
    (r'^(No|Nope|Nah)',
        ["Are you saying no just to be negative?", "Why not?"]),
    (r'(.*) computer(.*)',
        ["Are you really talking about me?", "Does it seem strange to talk to a computer?", "How do computers make you feel?", "Do you feel threatened by computers?"]),
    (r'Is it (.*)',
        ["Do you think it is {0}?", "Perhaps it's {0} -- what do you think?", "If it were {0}, what would you do?", "It could well be that {0}."]),
    (r'It is (.*)',
        ["You seem very certain.", "If I told you that it probably isn't {0}, what would you feel?"]),
    (r'Can you (.*)',
        ["What makes you think I can't {0}?", "If I could {0}, then what?", "Why do you ask if I can {0}?"]),
    (r'Can I (.*)',
        ["Perhaps you don't want to {0}.", "Do you want to be able to {0}?", "If you could {0}, would you?"]),
    (r'You are (.*)',
        ["Why do you think I am {0}?", "Does it please you to think that I'm {0}?", "Perhaps you would like me to be {0}.", "Perhaps you're really talking about yourself?"]),
    (r'You\'?re (.*)',
        ["Why do you say I am {0}?", "Why do you think I am {0}?", "Are we talking about you, or me?"]),
    (r'I don\'?t (.*)',
        ["Don't you really {0}?", "Why don't you {0}?", "Do you want to {0}?"]),
    (r'I feel (.*)',
        ["Good, tell me more about these feelings.", "Do you often feel {0}?", "When do you usually feel {0}?", "When you feel {0}, what do you do?"]),
    (r'I have (.*)',
        ["Why do you tell me that you've {0}?", "Have you really {0}?", "Now that you have {0}, what will you do next?"]),
    (r'I would (.*)',
        ["Could you explain why you would {0}?", "Why would you {0}?", "Who else knows that you would {0}?"]),
    (r'I (have|would|could|can|should)(n\'?t| ?not) (.*)',
        ["Could you explain why you {0}n't {2}?", "Would you like to {2}?", "Who else knows that you {0}n't {2}?"]),
    (r'I (guess|suppose|think) (.*)',
        ["You sound rather unsure of yourself. Why is that?", "Are you confident about that?"]),
    (r'Is there (.*)',
        ["Do you think there is {0}?", "It's likely that there is {0}.", "Would you like there to be {0}?"]),
    (r'(.*) always(.*)',
        ["Can you think of a specific example?", "When?", "What incident are you thinking of?", "Really, always?"]),
    (r'(.*) (alike|same|similar)(.*)',
        ["In what way?", "What resemblence do you see?", "What does that similarity suggest to you?", "What other connections do you see?", "What do you suppose that resemblence means?", "How?"]),
    (r'(.*) (everyone|everybody|nobody|no one)(.*)',
        ["You have a particular person in mind, don't you?", "Really? Is that statement not a bit extreme?", "Are you thinking of anyone in particular?", "Really?"]),
    (r'My (.*)',
        ["I see, your {0}.", "Why do you say that your {0}?", "When your {0}, how do you feel?"]),
    (r'You (.*)',
        ["We should be discussing you, not me.", "Why do you say that about me?", "Why do you care whether I {0}?"]),
    (r'Why (.*)',
        ["Why don't you tell me the reason why {0}?", "Why do you think {0}?"]),
    (r'I (want|desire|wish for|hope that) (.*)',
        ["What would it mean to you if you got {1}?", "Why do you want {1}?", "What would you do if you got {1}?", "If you got {1}, then what would you do?"]),
    (r'(.*) mother(.*)',
        ["Tell me more about your mother.", "What was your relationship with your mother like?", "How do you feel about your mother?", "How does this relate to your feelings today?", "Good family relations are important."]),
    (r'(.*) father(.*)',
        ["Tell me more about your father.", "How did your father make you feel?", "How do you feel about your father?", "Does your relationship with your father relate to your feelings today?", "Do you have trouble showing affection with your family?"]),
    (r'(.*) child(.*)',
        ["Did you have close friends as a child?", "What is your favorite childhood memory?", "Do you remember any dreams or nightmares from childhood?", "Did the other children sometimes tease you?", "How do you think your childhood experiences relate to your feelings today?"]),
    (r'(.*) (surpris|shock|astound|excit)ing(.*)',
        ["Why is it so {1}ing?", "Is it really that {1}ing", "Would you rather it elicited a different response?"]),
    (r'(.*)\?',
        ["Why do you ask that?", "Please consider whether you can answer your own question.", "Perhaps the answer lies within yourself?", "Why don't you tell me?"]),
    (r'quit',
        ["Thank you for talking with me.", "Good-bye.", "Thank you, have a good day!"]),
    (r'(.*)',
        ["Please tell me more.", "Let's change focus a bit... Tell me about your family.", "Can you elaborate on that?", "Why do you say that {0}?", "I see.", "Very interesting.", "{0}.", "I see. And what does that tell you?", "I see. And why is that?", "How does that make you feel?", "How do you feel when you say that?"])
]