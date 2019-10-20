import re
import json

# load file
with open ("/home/main/Downloads/final.response2", "r") as infile:
    raw_text=infile.read()

# Split up all apps
regex = re.compile(r'{.*?}', re.MULTILINE | re.DOTALL)
apps = re.findall(regex, raw_text)

# Create a list of valid json objects
app_objects = [json.loads(app) for app in apps]

# See what it does
print(app_objects)
for app in app_objects:
    name = app['package_name']
    url = app['url']
    print("wget --content-disposition \"{}\" -O {}.apk"
          .format(url, name))
