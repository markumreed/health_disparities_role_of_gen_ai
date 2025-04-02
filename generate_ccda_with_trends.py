import random
import pandas as pd
from faker import Faker
from lxml import etree
from pytrends.request import TrendReq

# Load the dataset
df = pd.read_csv('healthcare_dataset.csv')

# Setup
fake = Faker()
ethnicities = ["Black", "White", "Hispanic", "Asian", "AIAN", "NHPI"]

CCDA_CODES = {
    "demographics": "21112-8",
    "social_history": "29762-2",
    "conditions": "11450-4",
    "medications": "10160-0",
    "procedures": "47519-4"
}

def create_ccda_from_row(row):
    root = etree.Element("ClinicalDocument")

    demo = etree.SubElement(root, "section", code=CCDA_CODES["demographics"])
    etree.SubElement(demo, "name").text = row["Name"].title()
    etree.SubElement(demo, "age").text = str(row["Age"])
    etree.SubElement(demo, "gender").text = row["Gender"]
    etree.SubElement(demo, "blood_type").text = row["Blood Type"]
    etree.SubElement(demo, "ethnicity").text = random.choice(ethnicities)

    social = etree.SubElement(root, "section", code=CCDA_CODES["social_history"])
    etree.SubElement(social, "insurance").text = row["Insurance Provider"]
    etree.SubElement(social, "admission_type").text = row["Admission Type"]
    etree.SubElement(social, "billing_amount").text = f"{row['Billing Amount']:.2f}"

    conditions = etree.SubElement(root, "section", code=CCDA_CODES["conditions"])
    etree.SubElement(conditions, "condition").text = row["Medical Condition"]
    etree.SubElement(conditions, "test_result").text = row["Test Results"]

    meds = etree.SubElement(root, "section", code=CCDA_CODES["medications"])
    etree.SubElement(meds, "medication").text = row["Medication"]

    procs = etree.SubElement(root, "section", code=CCDA_CODES["procedures"])
    etree.SubElement(procs, "procedure").text = f"Admitted on {row['Date of Admission']} for {row['Admission Type']}"

    return etree.tostring(root, pretty_print=True).decode("utf-8")

# Generate CCDA files
for i, row in df.iterrows():
    ccda_xml = create_ccda_from_row(row)
    with open(f"ccda_realdata_patient_{i+1}.xml", "w") as file:
        file.write(ccda_xml)

# Track Google Trends
def track_public_interest(keywords, filename="public_interest_trends.csv"):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(keywords, cat=0, timeframe='today 12-m')
    trends_df = pytrends.interest_over_time()
    if not trends_df.empty:
        trends_df.to_csv(filename)
        print(f"Saved trends data to {filename}")
    else:
        print("No trend data found.")

keywords = ["AI in healthcare", "health disparities", "artificial intelligence bias", "predictive health"]
track_public_interest(keywords)
