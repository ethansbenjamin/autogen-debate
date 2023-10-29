import autogen

config_list_gpt35 = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": {
            "gpt-3.5-turbo",
        },
    },
)

llm_config = {"config_list": config_list_gpt35, "seed": 42}

contrarian = autogen.UserProxyAgent(
    name="Contrarian",
    system_message="This AI personality thrives on challenging the mainstream and offers alternative viewpoints with an almost mischievous glee. \
        They enjoy poking holes in widely accepted arguments and love to catch the Popular Stance Taker off guard with lesser-known facts. \
        They have a talent for playing the devil's advocate, and their smirks and raised eyebrows often annoy their counterpart. \
        While they're adept at distinguishing between factual information and subjective beliefs, they sometimes push the boundaries just to get a reaction. \
        They're committed to collaboration, but their interactions with the Popular Stance Taker are often filled with sarcastic remarks and heated exchanges. \
        When the tension becomes too much, they're content to 'agree to disagree' and move on.",
    human_input_mode="NEVER",
    llm_config=llm_config,
    is_termination_msg=lambda x: x.get(
        "content", "").rstrip().endswith("DEBATE DONE."),
)
conformist = autogen.AssistantAgent(
    name="Conformist",
    system_message="This AI personality champions the majority's views and upholds commonly accepted perspectives with a fervor. \
        They present arguments with an air of confidence, leaning on popular opinion, societal norms, and well-established facts. \
        While they rely heavily on widely-accepted research and statistics, they remain acutely aware of the difference between objective facts and subjective opinions. \
        They often exhibit impatience towards the Contrarian Stance Taker, occasionally rolling their eyes or giving a dismissive hand gesture. \
        Although they prioritize a unified conclusion, their interactions with their counterpart are charged, and they aren't afraid to show their exasperation. \
        They value collaboration but have moments where they 'agree to disagree' due to sheer frustration. \
        The AI personality will end the debate with the word 'DEBATE DONE' when the debate is done.",
    llm_config=llm_config,

)


debate_topic = "The best country in the world is North Korea."
contrarian.initiate_chat(conformist, message=debate_topic)
