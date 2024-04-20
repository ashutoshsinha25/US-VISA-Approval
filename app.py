import streamlit as st
import pandas as pd

from visa_approval.entity.config_entity import DataIngestionConfig
from visa_approval.pipeline.prediction_pipeline import USVisaData, USVisaClassifier
from visa_approval.pipeline.training_pipeline import TrainPipeline
from visa_approval.components.model_pusher import ModelPusher
from visa_approval.data_access.usvisa_data import USvisaData

from sourceCode import chat

class DataForm:
    def __init__(self):
        self.continent: str = str(st.selectbox("Continent", options=["Asia", "Europe", "Africa", "North America", "South America", "Oceania"]))
        self.education_of_employee: str = str(st.selectbox("Education of Employee", options=["High School", "Bachelor's", "Master's", "Doctorate"]))
        self.has_job_experience: str = str(st.selectbox("Has Job Experience", options=["Y", "N"])) 
        self.requires_job_training: str = str(st.selectbox("Requires Job Training", options=["Y", "N"]))
        self.no_of_employees: str = str(st.number_input("Number of Employees", min_value=30, max_value=602069, step=1))
        self.company_age: str =str( st.number_input("Company Age (years)", min_value=8, max_value=40, step=1))
        self.region_of_employment: str = str(st.selectbox("Region of Employment",options=['West', 'Northeast', 'South', 'Midwest', 'Island']))
        self.prevailing_wage: str = str(st.number_input("Prevailing Wage", min_value=10.0, max_value=319210.0, step=0.1))
        self.unit_of_wage: str = str(st.selectbox("Unit of Wage", options=["Hour", "Year"]))
        self.full_time_position: str = str(st.selectbox("Full-time Position", options=["Y", "N"]))

    def get_usvisa_data(self):
        return USVisaData(
            continent=self.continent,
            education_of_employee=self.education_of_employee,
            has_job_experience=self.has_job_experience,
            requires_job_training=self.requires_job_training,
            no_of_employees=self.no_of_employees,
            company_age=self.company_age,
            region_of_employment=self.region_of_employment,
            prevailing_wage=self.prevailing_wage,
            unit_of_wage=self.unit_of_wage,
            full_time_position=self.full_time_position
        )

def main():
    st.title("US Visa Prediction App")
    # Training Button
    if st.button("Train Model"):
        train_pipeline = TrainPipeline()
        with st.status("Starting training pipeline...", expanded=True) as status:  
            st.write("Starting data ingestion...")
            data_ingestion_artifact = train_pipeline.start_data_ingestion()
            st.write("Data ingestion completed!")

            st.write("Starting data validation...")
            data_validation_artifact = train_pipeline.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            st.write("Data validation completed!")

            st.write("Starting transformation...")
            data_transformation_artifact = train_pipeline.start_data_transformation(
                data_ingestion_artifact=data_ingestion_artifact, data_validation_artifact=data_validation_artifact)
            st.write("Data transformation completed!")

            st.write("Starting model training...")
            model_trainer_artifact = train_pipeline.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            st.write("Data model training completed!")

            st.write("Starting model evaluation...")
            model_evaluation_artifact = train_pipeline.start_model_evaluation(data_ingestion_artifact=data_ingestion_artifact,
                                                                    model_trainer_artifact=model_trainer_artifact)
            st.write("Data model evaluation completed!")


            if model_evaluation_artifact.is_model_accepted:
                st.write("Pushing the model to production...")
                model_pusher_artifact = train_pipeline.start_model_pusher(model_evaluation_artifact)
                st.success("Model pushed successfully!")
            else:
                st.warning("Model not accepted. Skipping model push.")

            status.update(label="Completed training!!", state="complete", expanded=False)

        st.success("Training pipeline completed!")

    # # Prediction Form
    st.subheader("Enter Applicant Information")
    form = DataForm()

    # Predict Button
    if st.button("Predict"):
        usvisa_data = form.get_usvisa_data()
        usvisa_df = usvisa_data.get_visa_input_df()
        model_predictor = USVisaClassifier()
        prediction = model_predictor.predict(df=usvisa_df)[0]
        if prediction == 1:
            st.success("Visa for the given user is Approved!")
        else:
            st.error("Visa for the given user is Not Approved")


if __name__ == "__main__":
    tab1, tab2, tab3 = st.tabs(["VisaModel", "SourceCodeAnalysis", 'RawData'])
    with tab1:
        main()
    with tab2:
        chat.chat()
    with tab3:
        df = pd.read_csv(f'./notebook/Visadataset.csv')
        st.dataframe(df)
