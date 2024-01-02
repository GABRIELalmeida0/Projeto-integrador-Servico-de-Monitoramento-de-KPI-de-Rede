import json
import pandas as pd 
from os import listdir

df = pd.DataFrame({"delay": [], "jitter": [], "loss": [], "ssim": []})

for dir in sorted(listdir("videos/"),key=lambda x:int(x.split("-")[-1])):
    if "metrics.txt" in [file for file in listdir(f"videos/{dir}")]:

        with open(f'videos/{dir}/metrics.txt', 'r') as file:
            content = file.read()

        start_index = content.find('{')

        json_content = content[start_index:]

        data = json.loads(json_content)

        df_ssim = data['global']['ssim']['ssim_avg']

        average_value = df_ssim['average']

        info_first_line = {info.split("-")[0].strip():info.split("-")[1] for info in content.split('\n')[0].split(",")}
        info_first_line.update({"ssim":average_value})


        df = pd.concat([df,pd.DataFrame([info_first_line])],ignore_index=True)
df.index.name = "index"
print(df)
df.to_csv("ssim_for_mos")
