languages = [
    "C", "C++", "D", "V", "Fortran", "Verilog", "Prolog", "Forth", "Go", "Rust", "Zig",
    "Porth", "Callisto", "YSL", "YSL-R", "YSL-C", "Bash", "Batch", "Haskell", "OCaml",
    "Python", "JavaScript", "Ruby", "HTML", "CSS", "Markdown", "PowerShell", "Brainfuck",
    "Malbolge", "Jupyter Notebook", "Vue", "Vala", "uxntal", "Concata", "APL", "WPL",
    "Modal", "Carbon", "Nim"
]
libraries = [
    "ncurses", "SDL2", "asyncio", "vibe.d", "discord.js", "discord.py", "Unity",
    "Unreal Engine", "Rails", "stb", "Godot", "YSL-M"
]
people = [
    "Bill Gates", "Linus Torvalds", "Brendan Eich", "Richard Stallman",
    "Bjarne Stroustrup", "Ada Lovelace", "Alan Turing", "John von Neumann", "Elon Musk",
    "Yeti", "soxfox",
]
companies = ["Microsoft", "Google", "Meta", "Shopify", "YouTube", "Discord", "NASA"]
issues = ["memory safety", "race condition", "goto statement", "segmentation fault"]
takes = [
    "Did you know that $L is the worst programming language in the world?",
    "Did you know that $L is the best programming language in the world?",
    "Why are schools not teaching $A? We're setting our kids up to fail.",
    "$L users couldn't even print Hello World in $L.",
    "$A is toxic for humanity. This is not an opinion, it's an absolute truth.",
    "$A users should be sent to prison for life.",
    "$A users don't understand programming.",
    "I have been coding in $L for $N years and I still do not understand why people use $A.",
    "$A fans are smarter than the average programmers.",
    "I'm sick of these pseudo-intellectual $A users, sitting in their ivory towers, looking down on the rest of us.",
    "The $A community is toxic.",
    "The fact that we're still using $A in 2024 is a problem.",
    "Average $A user vs average $A enjoyer.",
    "Every tech stack should include $A.",
    "People may disagree with the things I say, but I'd like to remind the haters that I have worked on a one-billion line $L codebase.",
    "$A is a $I disaster waiting to happen.",
    "I have been working with $A for over $N years, AMA.",
    "Well written $L is what heaven looks like.",
    "$P was the first true computer scientist.",
    "$P, inventor of $A is who we should all aspire to be like.",
    "$A was pioneered by $P",
    "Coding in $L is mental torture.",
    "I have a PhD in Computer Science and I'm still not sure how $A works.",
    "Honestly, $A fans are insufferable",
    "Everyone should learn $L as their first language.",
    "$L is not a programming language. Change my mind.",
    "AITA from banning my GF from using $L?",
    "I just started a new job at $C. My boss, $P just told me to refactor 58235 lines of $L. Kill me.",
    "$P debunked $A a long time ago.",
    "$A fans are quickly taking over the tech world and that's good.",
    "I'm genuinely surprised to hear that there are programmers who use $A",
    "I'm genuinely surprised to hear that there are programmers who don't use $A",
    "IMO, $P needs to start looking at $A.",
    "Oh, your code is written in $L? Sorry, I don't speak stupid.",
    "I think I'm addicted to working with $A. Does anyone else feel the same?",
    "$A is just $A mixed with $A.",
    "I had an interviewer laugh in my face when I said I use $A.",
    "I have an irrational hatred for $A.",
    "I just purchased the domain name $A.net. I'm going to make a fortune.",
    "$A fans don't deserve to be in tech.",
    "If Jesus was alive today, he would be using $A.",
    "I love $P so much!",
    "We should really stop listening to $P. They told us to use $A, after all.",
    "I'm not an $A fan, but I'm a $A fan.",
    "Coding in $L is like walking over hot coals.",
    "After just a few hours, I've optimised my $L codebase $Nx. Writing up a blog post as we speak.",
    "Where are all the $A jobs? Are people really looking for $A?",
    "I just donated $$2348 to $P's Patreon. They deserve it.",
    "Did you know $L is one of the oldest programming languages in the world?",
    "$C uses $A so it must be good.",
    "$A doesn't need $A, it's perfect already.",
    "Gen Z kids don't understand $A.",
    "The perfect programming language is $L mixed with $L.",
    "One of my greatest achievements is becoming a moderator of r/$A.",
    "I'm looking for a new job. I'm not sure if I should apply to $C. I've heard they're $A haters.",
    "Started learning $L yesterday. Already built an AI that can solve $I. Should I drop out of school?"
]

arrs = ["languages", "libraries", "people", "companies", "issues", "takes"]

for name in arrs:
    arr = globals()[name]
    joined = "".join(el + "\\0" for el in arr)
    joined = joined.replace('"', '\\"')
    print(f'c"{joined}" -> {name}')
    print(f'const {name}_len {len(arr)}')
    print()
