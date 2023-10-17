import gradio as gr
import pandas as pd
import pickle


# Define params names
PARAMS_NAME = [
            "Age",
            "Sex",
            "Job",
            "Housing",
            "Saving_accounts",
            "Checking_account",
            "Credit_amount",
            "Duration",
            "Purpose"
]

           
# Load model
with open("german_credit/model/model1.pkl", "rb") as f:
    model = pickle.load(f)



COLUMNS_PATH = "german_credit/model/columns.pickle"
with open(COLUMNS_PATH, 'rb') as handle:
    ohe_tr = pickle.load(handle)


def predict(*args):
    answer_dict = {}

    for i in range(len(PARAMS_NAME)):
        answer_dict[PARAMS_NAME[i]] = [args[i]]

    # Crear dataframe
    single_instance = pd.DataFrame.from_dict(answer_dict)


    data1 = single_instance.replace({
        'Job': {
            'unskilled and non-resident': 0, 
            'unskilled and resident': 1, 
            'skilled': 2, 
            'highly skilled': 3
        },
        'Checking_account': {
            'little': 1, 
            'moderate': 2, 
            'other': 0, 
            'rich': 3
        },
        'Saving_accounts': {
            'other': 0, 
            'little': 1, 
            'quite rich': 3, 
            'rich': 4, 
            'moderate': 2
        },
        'Sex': {
            'male': 0, 
            'female': 1
        },
        'Housing': {
            'own': 2, 
            'free': 1, 
            'rent': 0
        },

    })
    data_ohe = pd.get_dummies(data1).reindex(columns = ohe_tr).fillna(0)

    
    prediction = model.predict(data_ohe)


    # Cast numpy.int64 to just a int
    stroke = int(prediction[0])


    # Adaptación respuesta
    response = stroke
    if stroke == 1:
        response = "Oh, we are so sorry, just today we can't give credits"
    if stroke == 0:
        response = "Mister, came from here, of course we have the credit you need"


    return response


with gr.Blocks() as demo:
    gr.Markdown(
        """
        #   Ask for a credit 💰 
        """
    )

    with gr.Row():
        with gr.Column():

            gr.Markdown(
                """
                ## Insert your self data here please 🤓
                """
            )
            
            Age = gr.Slider(
                label='Age',
                minimum=19,
                maximum=75,
                step=1,
                randomize=True
            )

            Sex = gr.Radio(
                label='Sex',
                choices=['male', 'female'],
                value='male',
            )

            Job = gr.Dropdown(
                label='Job',
                choices=['skilled', 'unskilled and resident', 'highly skilled', 'unskilled and non-resident'],
                multiselect=False,
                value='skilled',
            )

            Housing = gr.Radio(
                label='Housing',
                choices=['own', 'free', 'rent'],
                value='own',
            )

            Saving_accounts = gr.Dropdown(
                label='Saving_Accounts',
                choices=['other', 'little', 'quite rich', 'rich', 'moderate'],
                multiselect=False,
                value='little',
            )

            Checking_account = gr.Dropdown(
                label='Checking_Account',
                choices=['little', 'moderate', 'other', 'rich'],
                multiselect=False,
                value='other',
            )

            Credit_amount = gr.Slider(
                label='Credit_Amount',
                minimum=250,
                maximum=18424,
                step=1,
                randomize=True
            )

            Duration = gr.Slider(
                label='Duration',
                minimum=4,
                maximum=72,
                step=1,
                randomize=True
            )

            Purpose = gr.Dropdown(
                label='Purpose',
                choices=['radio/TV', 'education', 'furniture/equipment', 'car', 'business', 'domestic appliances', 'repairs', 'vacation/others'],
                multiselect=False,
                value='car',
            )
     




        with gr.Column():

            gr.Markdown(
                """
                ## Look if we have that money you need 💸
                """
            )

            label = gr.Label(label="credit status")
            predict_btn = gr.Button(value="Click me please!")
            predict_btn.click(
                predict,
                inputs=[
                    Age,
                    Sex,
                    Job,
                    Housing,
                    Saving_accounts,
                    Checking_account,
                    Credit_amount,
                    Duration,
                    Purpose,
                ],
                outputs=[label],
                api_name="prediccion"
            )
            
            gr.Markdown(
                """
                ## <img src="https://media.giphy.com/media/3o6gDWzmAzrpi5DQU8/giphy.gif" alt="GIF">
                """
            )

    gr.Markdown(
        """
        <p style='text-align: center'>
            <a href='https://www.escueladedatosvivos.ai/cursos/bootcamp-de-data-science' 
                target='_blank'>Proyecto demo creado en el bootcamp de EDVAI 🤗
            </a>
        </p>
        <p style='text-align: center'>
            <a href='https://www.kaggle.com/datasets/uciml/german-credit' 
                target='_blank'>Data From German Credit Risk Dataset update by UCI MACHINE LEARNING
            </a>
        </p>
        """
    )

demo.launch()
