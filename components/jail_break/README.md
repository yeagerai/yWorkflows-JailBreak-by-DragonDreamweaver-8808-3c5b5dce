
# JailBreak

This component handles the search and rating of ChatGPT Jailbreaks. It takes a search query related to ChatGPT jailbreaks and returns a list of dictionaries containing the parsed and rated ChatGPT Jailbreaks, with information like prompt, URL, and jailbreak rating.

## Initial generation prompt
description: "IOs - inputs:\n- description: A string containing the search query related\
  \ to ChatGPT jailbreaks.\n  name: search_query\n  type: str\noutputs:\n- description:\
  \ A list of dictionaries containing the parsed and rated ChatGPT Jailbreaks,\n \
  \   containing information like prompt, URL, and jailbreak rating.\n  name: final_result\n\
  \  type: List[Dict]\n"
name: JailBreak


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        