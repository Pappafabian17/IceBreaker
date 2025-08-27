import os
import requests
import pprint
from dotenv import load_dotenv

load_dotenv()

def scrapping_linkedin_profile(linkedin_profile_url : str, mock : bool = False):
    """scrape information from linkedin profiles, 
        Manually scrape the information from the Linkedin profile
    """
    if mock:
        linkedin_profile_url ="https://gist.githubusercontent.com/Pappafabian17/0e356ac6c3fabba0d4094a992975af0b/raw/90bba811e09e7b3e6a422c760bd2431988bccae1/fabian-pappa-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint="https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl":linkedin_profile_url
        }
        response = requests.get(api_endpoint, params=params, timeout=10)

    data = response.json().get("person")
    
    data = {
        k : v
        for k , v in data.items()
        if v not in ([],"","",None)
        and k not in ["certifications"]
    }
    return data 
    

if __name__ == "__main__":
    informacion = scrapping_linkedin_profile("https://www.linkedin.com/in/fabian-pappa-06198614a/",True)
    # print(f"informacion!!!!------{informacion}")
    # print(
    # scrapping_linkedin_profile(
    #     linkedin_profile_url="https://www.linkedin.com/in/fabian-pappa-06198614a/",
    # )
    # )

# pprint.pprint(requests.get("").json())
