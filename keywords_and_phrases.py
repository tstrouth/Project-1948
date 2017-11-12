from PyDictionary import PyDictionary

dictionary = PyDictionary()

keywords_and_phrases = ["Guidance", "Not Caring", "Safe", "Inspired",
                            "Hate", "Scared","Mad", "Stress", "Happy", "Sad",
                            "Volunteering", "Altruism", "Loss", "Pride","Pain",
                            "Anger", "Fear", "Guilt", "Shame", "Down Syndrome",
                            "Anorexia", "Bulemia", "Recovery", "Resilency",
                            "Community", "Death", "Home & Belongings",
                            "Substance Abuse", "Trauma", "PTSD",
                            "Intergenerational Trauma", "Conflict",
                            "Sense of Belonging", "Marriage", "Connection",
                            "Refugee due to War", "Absense of Trust",
                            "Non-Acceptance", "Violence", "Grace",
                            "Acceptance", "Interfaith", "Adolescense", "LGBT",
                            "Childhood", "Multi-Cultural", "Unity", "Division",
                            "Balkanization", "Hierarchical", "Egalitarian",
                            "Individualism", "Betrayal", "Forgiveness",
                            "Social Injustice", "Activism",
                            "Conflict Resolution", "Absense of War",
                            "Dayton Peace Agreement", "Unemployment",
                            "Community Initiatives", "Community Participation",
                            "Poverty", "Income", "Discrimination",
                            "Anti-Semitism", "Rape", "Genocide", "Xenophobia",
                            "Denial", "Inquisitive", "Unknown", "Beautiful",
                            "Dark", "Disturbing", "Light", "Ethnicity",
                            "Disaster", "War", "Attack", "Enemies",
                            "Shootings", "Defense", "Grenades", "Natural",
                            "Flood", "Buildings", "Malls", "Government",
                            "Lack of Funding", "Military", "Petitions",
                            "Politics", "Census", "Constitution", "Corruption",
                            "Home", "Museum", "Relgious Institution",
                            "Synagogue", "Cemetary", "Church", "Cathedral",
                            "Mosque", "War-Torn", "Past", "Present", "Future",
                            "Hope", "Religion", "Religious Symbol", "Absence",
                            "Gender Inequality", "Careers", "Nepotism" ]
print(len(keywords_and_phrases))

for i in range(len(keywords_and_phrases)):
    new_list = []
    try:
        new_list = dictionary.synonym(keywords_and_phrases[i])
        if len(new_list) > 0:
            for j in range(len(new_list)):
                if (new_list[j] not in keywords_and_phrases
                    and new_list[j].title() not in keywords_and_phrases):
                    keywords_and_phrases.append(new_list[j].title())
    except TypeError:
        pass

f = open('Keywords_And_Phrases.csv', 'w')
for i in range(len(keywords_and_phrases)):
    f.write(keywords_and_phrases[i] + ',' + '\n')
f.close()
