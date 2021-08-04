import pandas as pd
import numpy as np
import time

def NewsMain(driver, topic):
    """Receive the driver and the topic, then return a dataset with links of the news in the choosen topic"""
    driver.get(f"https://duckduckgo.com/?q={topic}&t=brave&iar=news&ia=news")
    time.sleep(2)
    title_results = driver.find_elements_by_class_name("result__title")
    time_results = driver.find_elements_by_class_name("result__timestamp")
    for i in range(len(title_results)):
        if i == 0:
            news = np.array([[title_results[i].text, time_results[i].text]])
        else:
            news = np.append(news, [[title_results[i].text, time_results[i].text]], axis=0)
    news = pd.DataFrame(news)
    return news