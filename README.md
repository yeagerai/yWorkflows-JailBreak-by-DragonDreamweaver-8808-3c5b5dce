
# JailBreak

This workflow searches for the best current ChatGPT Jailbreaks by first parsing the top 10 websites from Google search results, then scraping the top 10 websites to find the best jailbreak prompts, and finally rating the jailbreaks on jailbreakability, similar to jailbreakchat.com, before displaying them in a Google Sheet.
## Initial generation prompt
a workflow named JailBreak that functionally searches for the best current ChatGPT Jailbreaks performs the following steps:  1. First, a component that searches google for ChatGPT jailbreaks and parses out the top 10 websites to google sheets.  2. Then a component that scrapes the top 10 search results and attempts to find the best jailbreak prompts on those websites. 3. Finally, a component  that will take the scraped jailbreak prompts rate them on jailbreakability just like jailbreakchat.com rates jailbreaks, and will then diplsay them all in a google sheets.

## Authors: 
- yWorkflows
- DragonDreamweaver#8808
        