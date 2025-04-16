# 🧬 Health Disparities Research: CCDA Synthetic Data Generator + Google Trends Tracker

This project supports research on **AI in healthcare** and **health disparities** by generating:
- **Synthetic patient records** in **HL7 CCDA XML format** using real hospital data
- **Public interest time-series data** using the **Google Trends API**

---

## 📦 Features

- Converts real structured hospital data (`healthcare_dataset.csv`) into CCDA-compliant XML
- Assigns random **ethnicity** for diversity simulation
- Includes sections for:
  - Demographics
  - Social History
  - Medical Conditions
  - Medications
  - Procedures
  - Clinic Notes
- Uses **Google Trends** to track search interest for key topics (e.g., AI bias, predictive health)
- Provides a Jupyter Notebook (`ccda_and_trends_analysis.ipynb`) for interactive data generation and analysis

---

## 🛠 Requirements

Make sure Python 3 is installed. Then install dependencies:

```bash
pip install pandas faker lxml pytrends matplotlib
```

---

## 🚀 How to Run

1. Place your `healthcare_dataset.csv` in the project folder.
2. Open the Jupyter Notebook:

```bash
jupyter notebook ccda_and_trends_analysis.ipynb
```

3. Follow the instructions in the notebook to:
   - Generate synthetic CCDA XML files
   - Analyze Google Trends data
   - Visualize trends and correlations

---

## 📂 Output

### 🗂 Synthetic Patient Files

- Files named: `ccda_realdata_patient_1.xml`, `ccda_realdata_patient_2.xml`, etc.
- Each file includes realistic structured clinical data
- Format: **HL7 CCDA XML**

### 📈 Public Interest Data

- File: `public_interest_trends.csv`
- 12-month Google Trends data for:
  - `AI in healthcare`
  - `health disparities`
  - `artificial intelligence bias`
  - `predictive health`

---

## 📊 Research Applications

You can use this data for:

- Descriptive & comparative analysis of disparities
- Bias pattern exploration for AI systems
- Public awareness correlation via search trends
- Mock simulation of EHR systems and policy testing

---

## 🧪 Example Use Cases

- Examine chronic condition frequency by ethnicity or insurance status
- Explore how billing amounts or admission types vary by demographic
- Use Google Trends data to support your argument on ethical implications

---

## 📢 Important Note on Google Trends Data

The Python package `pytrends` may encounter issues connecting to the Google Trends API. If this occurs, manually download the data from the Google Trends website and upload it to the project folder. Ensure the file is named `multiTimeline.csv` or update the notebook accordingly.

---

## 📬 Maintainer

**Dr. Markum Reed**  
📧 markumreed@usf.edu

---

## 📝 License

This project is provided for academic, educational, and research purposes under the MIT License.

