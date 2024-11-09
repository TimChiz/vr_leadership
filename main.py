from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Leadership scenarios data
leadership_scenarios = [
    {
        "id": 1,
        "title": "Scenario 1: Microaggression from a Male Colleague",
        "setting": "Office break room.",
        "characters": ["Emily (young woman)", "Tom (male colleague)"],
        "dialogue": [
            "Emily: (pouring coffee) Good morning, Tom! How was your weekend?",
            "Tom: (with a smirk) It must be nice to have a job like yours. I mean, it’s not too hard to look busy, right?",
            "Emily: (calmly) I work hard to earn my place here, Tom. I’d appreciate it if we could keep our comments focused on our work instead of making assumptions about my contributions.",
            "Tom: (surprised) Oh, I didn’t mean anything by it.",
            "Emily: I understand, but comments like that can be discouraging. Let’s support each other instead."
        ],
        "comment": "Emily addressed the microaggression directly and assertively, promoting respectful dialogue and setting clear boundaries."
    },
    {
        "id": 2,
        "title": "Scenario 2: Rejecting Advances and Dealing with Backlash",
        "setting": "Office hallway.",
        "characters": ["Sarah (young woman)", "Mike (male colleague)"],
        "dialogue": [
            "Mike: (leaning against the wall) Hey Sarah, wanna grab dinner sometime? Just the two of us?",
            "Sarah: (politely) Thanks for the invite, Mike, but I’d prefer to keep things professional.",
            "Mike: (offended) Oh, come on! Do you think you're too good for me or something?",
            "Sarah: (assertively) No, it’s not that. I value our working relationship and want to keep it that way. I hope you can respect my decision.",
            "Mike: (grumbling) Whatever.",
            "Sarah: (confidently walking away) I’m just setting boundaries. It’s important to feel comfortable at work."
        ],
        "comment": "Sarah remained professional and clear in her rejection, standing firm against pressure while maintaining her dignity."
    },
    {
        "id": 3,
        "title": "Scenario 3: Sexist Remarks from a Female Colleague",
        "setting": "Team meeting.",
        "characters": ["Lisa (young woman)", "Karen (female colleague)"],
        "dialogue": [
            "Karen: (scoffing) You really think your idea will work? I mean, isn’t that a bit ambitious for someone like you?",
            "Lisa: (calmly) I believe in my idea, and I’ve put in a lot of research to back it up. Everyone deserves to be taken seriously, regardless of their experience level.",
            "Karen: (dismissively) We’ll see about that.",
            "Lisa: (confidently) I’d appreciate your support instead of skepticism. We’re all here to contribute and grow as a team."
        ],
        "comment": "Lisa addressed the sexism assertively and invited collaboration, turning a negative comment into a constructive opportunity."
    },
    {
        "id": 4,
        "title": "Scenario 4: Microaggression from a Female Colleague",
        "setting": "Office workspace.",
        "characters": ["Mia (young woman)", "Jenna (female colleague)"],
        "dialogue": [
            "Jenna: (sarcastically) Wow, Mia, you really love those bright colors. Trying to distract us from your work?",
            "Mia: (smiling) I wear what makes me feel good. My work speaks for itself, and I hope we can celebrate each other’s styles instead of criticizing them.",
            "Jenna: (taken aback) I didn’t mean it like that.",
            "Mia: I know, but it’s important to create a supportive environment. Let’s uplift each other instead!"
        ],
        "comment": "Mia handled the microaggression gracefully, redirecting the conversation toward mutual support and understanding."
    },
    {
        "id": 5,
        "title": "Scenario 5: Male Teammate Undermining Equal Female Teammate",
        "setting": "Open workspace during a team discussion.",
        "characters": ["Emma (Female teammate)", "Liam (Male teammate)"],
        "dialogue": [
            "Emma: For the upcoming campaign, I think focusing on user-generated content could really boost engagement. I’ve seen some solid data showing its effectiveness for brands like ours.",
            "Liam: Interesting… but user-generated content can be a bit unpredictable, don’t you think? It’s a big risk to rely on something we can’t fully control.",
            "Emma: True, it can be unpredictable. But that’s part of what makes it engaging—it feels more authentic to users. I’ve looked at case studies where it worked well, and I’d be happy to share those if it helps.",
            "Liam: Sure, I mean, as long as we have a backup plan if it doesn’t work out.",
            "Emma: Absolutely, and that’s why I’m suggesting a phased approach. We can test and adapt based on results without committing everything upfront."
        ],
        "comment": "Emma’s responses show she’s both knowledgeable and prepared, calmly handling Liam’s subtle undermining with confidence."
    },
    {
        "id": 6,
        "title": "Scenario 6: Female Leader Being Undermined by Male Subordinate",
        "setting": "Conference room.",
        "characters": ["Sarah (Woman boss)", "Jake (Male subordinate)"],
        "dialogue": [
            "Sarah: So, for this project, I’d like us to aim for completion by the end of Q2. It’s ambitious, but we can make it with a focused effort.",
            "Jake: (Smirks slightly) End of Q2? Don’t you think that’s a bit unrealistic, Sarah? I mean, sure, it sounds good on paper.",
            "Sarah: (Keeps her tone calm) I’ve reviewed the numbers, Jake, and I’m confident it’s doable. We’ll manage progress weekly to stay on track.",
            "Jake: (Shrugs) Alright, if you say so. I just hope everyone’s ready to run at your pace.",
            "Sarah: (Maintaining eye contact) I’m setting the pace for the team. Let’s focus on making this work together."
        ],
        "comment": "Sarah confidently addresses the undermining and keeps the focus on moving the project forward."
    },
    {
        "id": 7,
        "title": "Scenario 7: Male Boss Asking for Personal Favors in Exchange for Female Employee Career Advancement",
        "setting": "Mr. Reynolds's office, after-hours.",
        "characters": ["Laura (Employee)", "Mr. Reynolds (Male boss)"],
        "dialogue": [
            "Mr. Reynolds: Laura, you know you’re doing really well here. I see a lot of potential in you, and there could be some exciting opportunities opening up soon… if you’re willing to put in some extra effort.",
            "Laura: (Slightly uncomfortable, but maintaining her professionalism) Thank you, Mr. Reynolds. I’m fully committed to the team’s success and am willing to work hard for any advancement.",
            "Mr. Reynolds: (Leaning in, his tone suggestive) That’s good to hear. Sometimes, a little personal cooperation can make all the difference in accelerating a career, you know?",
            "Laura: (Steady, firm tone) I appreciate the feedback, but if we’re discussing my career development, I’d prefer to keep the conversation focused on my performance and qualifications.",
            "Mr. Reynolds: (Smirking) Well, Laura, not everyone sees career advancement as just a matter of job performance. Think about it.",
            "Laura: (Maintains eye contact, unwavering) Mr. Reynolds, I’m committed to professional growth based on merit. If there’s any concern about my performance, I’d be happy to review my recent work and discuss how I can improve."
        ],
        "comment": "Laura keeps her response professional, clearly rejects the advance, and reframes the conversation back to her performance."
    },
    {
        "id": 8,
        "title": "Scenario 8: Handling Mansplaining in the Meeting",
        "setting": "A team meeting room. Alice is presenting a strategy for an upcoming project.",
        "characters": ["Alice (Team lead)", "Tom (Male colleague)"],
        "dialogue": [
            "Alice: For the next quarter, I believe focusing on digital outreach will give us the best ROI. I’ve laid out a step-by-step plan to implement this, starting with our website and social media platforms.",
            "Tom: (Interrupting, leaning forward) Right, but digital outreach can be tricky. You see, the key is to engage audiences in a way that makes them feel personally connected to the brand. I can explain how that works if you'd like.",
            "Alice: (Smiling politely) Thanks, Tom, I’m aware of those principles. That’s why I’ve already incorporated engagement tactics into the strategy—let me walk everyone through those now.",
            "Tom: (Nods, slightly taken aback) Oh, of course. I was just making sure we’re all on the same page.",
            "Alice: Absolutely. And I think once you see the full plan, it’ll be clear how we’re addressing engagement directly."
        ],
        "comment": "Alice maintains authority and asserts her expertise while handling mansplaining both in the meeting and privately afterward."
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scenarios', methods=['GET'])
def get_scenarios():
    return jsonify(leadership_scenarios)

@app.route('/scenario/<int:scenario_id>', methods=['GET'])
def view_scenario(scenario_id):
    scenario = next((item for item in leadership_scenarios if item["id"] == scenario_id), None)
    if scenario is None:
        return "Scenario not found!", 404
    return render_template('view_scenario.html', scenario=scenario)

if __name__ == '__main__':
    app.run(debug=True)