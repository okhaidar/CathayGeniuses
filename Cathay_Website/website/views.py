from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import pandas as pd
from . import db
import json
import os
views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():

    '''# Get the path to the static directory
    static_folder = app.static_folder
    # Build the path to the Excel file
    file_path = os.path.join(static_folder, 'data/data.xlsx')
    # Read the Excel file
    df = pd.read_excel(file_path)
    # Iterate over the DataFrame rows
    for i, row in df.iterrows():
        row_num = i/3 + 1
        # The image URL is in the 'img2ForPLP' column
        exec(f"row_{row_num}_image{i+1} = '{row['img2ForPLP']}'")
        # The product names are in the 'baseProduct' column
        exec(f"row_{row_num}_name{i+1} = '{row['baseProduct']}'")
        # The product descriptions are in the 'description' column
        exec(f"row_{row_num}_description{i+1} = '{row['description']}'")'''
    #row_1_image_1="/medias/HP00221-02.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wzOTQwOHxpbWFnZS9qcGVnfGFHUTNMMmd4TWk4eE1EWXdOekF5TXpRMU5qSTROaTlJVURBd01qSXhJREF5TG1wd1oxOUJUVXd0UTI5dWRtVnlkQzB5T1RSWGVERTVOVWd8ZTBkNmFmYzYzMTM4ZjJhYzk3MmZhNDQ5MDUxYzI4YmZiNjc1OWNlZjY0MjU0NzcyMTFkNTBkMzc4NWNmYTJhYw"
    #row_1_image_2="/medias/RAH-Xmas-Dinner-Generic-2.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3w3Mjc3OXxpbWFnZS9qcGVnfGFESXdMMmcwTUM4eE1qTTVOVE00TmpjMk5UTTBNaTlTUVVnZ1dHMWhjeUJFYVc1dVpYSWdSMlZ1WlhKcFl5QXlMbXB3WjE5QlRVd3RRMjl1ZG1WeWRDMHlPVFJYZURFNU5VZ3xmNTc5OWQzMzI1YTcwZmI2N2Q4NDA5N2EwOTcxZTU3Mjg3OGM5OGZhZjhkZTAwM2Q3NjhkNzc1MDM5ZjMzYmEx"
    #row_1_image_3="/medias/Andy-Warhol-Chardonnay.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wyMzMyMnxpbWFnZS9qcGVnfGFEQTBMMmhsT1M4eE1EWXdOakU1T0RNMU9EQTBOaTlCYm1SNUlGZGhjbWh2YkNCRGFHRnlaRzl1Ym1GNUxtcHdaMTlCVFV3dFEyOXVkbVZ5ZEMweU9UUlhlREU1TlVnfDljYjYyNTVlMmNlZGJkZmNlYzBkYTdkOWIwYzhjNWU5ZjI5OTc2ZDUxZmJlNDg1NTkwZmMxNTk3YzM1NWZiM2U"
    
    row_1_image_1="/medias/HP00221-02.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wzOTQwOHxpbWFnZS9qcGVnfGFHUTNMMmd4TWk4eE1EWXdOekF5TXpRMU5qSTROaTlJVURBd01qSXhJREF5TG1wd1oxOUJUVXd0UTI5dWRtVnlkQzB5T1RSWGVERTVOVWd8ZTBkNmFmYzYzMTM4ZjJhYzk3MmZhNDQ5MDUxYzI4YmZiNjc1OWNlZjY0MjU0NzcyMTFkNTBkMzc4NWNmYTJhYw"
    row_1_image_1_name="CSW_0968"
    row_1_image_1_description="14 Original Tea Bags"

    row_1_image_2="/medias/RAH-Xmas-Dinner-Generic-2.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3w3Mjc3OXxpbWFnZS9qcGVnfGFESXdMMmcwTUM4eE1qTTVOVE00TmpjMk5UTTBNaTlTUVVnZ1dHMWhjeUJFYVc1dVpYSWdSMlZ1WlhKcFl5QXlMbXB3WjE5QlRVd3RRMjl1ZG1WeWRDMHlPVFJYZURFNU5VZ3xmNTc5OWQzMzI1YTcwZmI2N2Q4NDA5N2EwOTcxZTU3Mjg3OGM5OGZhZjhkZTAwM2Q3NjhkNzc1MDM5ZjMzYmEx"
    row_1_image_2_name="Regal Airport Hotel"
    row_1_image_2_description="Aficionado is one "

    row_1_image_3="/medias/Andy-Warhol-Chardonnay.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wyMzMyMnxpbWFnZS9qcGVnfGFEQTBMMmhsT1M4eE1EWXdOakU1T0RNMU9EQTBOaTlCYm1SNUlGZGhjbWh2YkNCRGFHRnlaRzl1Ym1GNUxtcHdaMTlCVFV3dFEyOXVkbVZ5ZEMweU9UUlhlREU1TlVnfDljYjYyNTVlMmNlZGJkZmNlYzBkYTdkOWIwYzhjNWU5ZjI5OTc2ZDUxZmJlNDg1NTkwZmMxNTk3YzM1NWZiM2U"
    row_1_image_3_name="Cuvaison Estate"
    row_1_image_3_description="world-renown region of Carneros in Napa Valley"

    row_2_image_1="/medias/KINOBI-KV.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wxNjQ5OXxpbWFnZS9qcGVnfGFHRmxMMmcxT1M4eE1UTXdNakExTVRJNE1qazNOQzlMU1U1UFFrbGZTMVl1YW5CblgwRk5UQzFEYjI1MlpYSjBMVEk1TkZkNE1UazFTQXw2MzQ2MWQ4NDI0ZDU1MDM5ZDM3ZGMxZWVmODUyZWU1MzI1ZDhiNWQ3Y2JjMDc5MzBmNGRlMDJlMjFhMzYyNDg2"
    row_2_image_1_name="Ki no Bi"
    row_2_image_1_description="A sophisticated blend of botanicals that offers a unique gin experience."

    row_2_image_2="/medias/Image-Marques-de-Caceres-Crianza.png-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wxMTI4N3xpbWFnZS9wbmd8YUdVMkwyZzJaaTh4TVRBME5ERTNOVGN3T0RFNU1DOUpiV0ZuWlNCTllYSnhkV1Z6SUdSbElFTmhZMlZ5WlhNZ1EzSnBZVzU2WVM1d2JtZGZRVTFNTFVOdmJuWmxjblF0TWprMFYzZ3hPVFZJfGY4MmM0MDU1N2MzODhkNzFhMDNjNjgzNWU5OWQyOWY4NGQ2Nzk2M2QyOWYxNDY3YzFhZWI5ZmFmYTg1ZDQxNTA"
    row_2_image_2_name="Marques de Caceres"
    row_2_image_2_description="A classic red wine that embodies the richness of Spanish vineyards."

    row_2_image_3="/medias/OriginalSizeJPEG-SainteMarguerite-2022-LifestyleProduct-012.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3w1NDMxfGltYWdlL2pwZWd8YUdNd0wyZzNaQzh4TURrNU1qUXpPREExTURnME5pOVBjbWxuYVc1aGJGTnBlbVZLVUVWSExWTmhhVzUwWlUxaGNtZDFaWEpwZEdWZk1qQXlNbDlNYVdabGMzUjViR1ZRY205a2RXTjBMVEF4TWk1cWNHZGZRVTFNTFVOdmJuWmxjblF0TWprMFYzZ3hPVFZJfDVlZTQ2OWJiNDI5MTg1NmVhMjBhYzUwOTgyN2RmZTA2MzM4ZDE4MTQxNzNkMzRlNWU2NjczM2QwZjdlZjQyYWQ"
    row_2_image_3_name="Maison Sainte Marguerite"
    row_2_image_3_description="A refreshing white wine with a hint of citrus and floral notes."

    row_3_image_1="/medias/NTCTWG9092-Joy-of-Christmas-Tea-2.jpg.webp-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3w2MTYwfGltYWdlL3dlYnB8YUdabUwyaGxaQzh4TURnNU5EWXdNRGd6TVRBd05pOU9WRU5VVjBjNU1Ea3lJRXB2ZVNCdlppQkRhSEpwYzNSdFlYTWdWR1ZoSURJdWFuQm5MbmRsWW5CZlFVMU1MVU52Ym5abGNuUXRNamswVjNneE9UVkl8NTg0OWU4NDUxZmRiNjcyMDg1M2EzYmFjOTc5Njc4MmJlMTI4MjQzNzcyMzJkMmJmNzliMDE5NTM1NjI3NGIzYw"
    row_3_image_1_name="Tea WG"
    row_3_image_1_description="Joy of Christmas Tea, an aromatic blend capturing the essence of the holiday season."

    row_3_image_2="/medias/Andy-Warhol-Chardonnay.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wyMzMyMnxpbWFnZS9qcGVnfGFEQTBMMmhsT1M4eE1EWXdOakU1T0RNMU9EQTBOaTlCYm1SNUlGZGhjbWh2YkNCRGFHRnlaRzl1Ym1GNUxtcHdaMTlCVFV3dFEyOXVkbVZ5ZEMweU9UUlhlREU1TlVnfDljYjYyNTVlMmNlZGJkZmNlYzBkYTdkOWIwYzhjNWU5ZjI5OTc2ZDUxZmJlNDg1NTkwZmMxNTk3YzM1NWZiM2U"
    row_3_image_2_name="Cuvaison Estate"
    row_3_image_2_description="Andy Warhol Chardonnay, a vibrant and full-bodied wine characterized by its rich flavors and artistic label."

    row_3_image_3="/medias/HP00221-02.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wzOTQwOHxpbWFnZS9qcGVnfGFHUTNMMmd4TWk4eE1EWXdOekF5TXpRMU5qSTROaTlJVURBd01qSXhJREF5TG1wd1oxOUJUVXd0UTI5dWRtVnlkQzB5T1RSWGVERTVOVWd8ZTBkNmFmYzYzMTM4ZjJhYzk3MmZhNDQ5MDUxYzI4YmZiNjc1OWNlZjY0MjU0NzcyMTFkNTBkMzc4NWNmYTJhYw"
    row_3_image_3_name="Fook Ming Tong"
    row_3_image_3_description="Premium Chinese tea, offering a balanced blend of taste and aroma for a calming tea experience."

    row_4_image_1="/medias/ChanteloupXXO-MARTELL-Packshot-Bottle-PNG-HR-70cl-BOTTLEFRONT-TRANSPARENT.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wzOTE2fGltYWdlL2pwZWd8YUROaUwyZ3hPQzg1TnpVNE1EUTBOemd5TmpJeUwwTm9ZVzUwWld4dmRYQllXRThnVFVGU1ZFVk1UQ0JRWVdOcmMyaHZkQ0JDYjNSMGJHVWdVRTVISUVoU0lEY3dZMndnUWs5VVZFeEZSbEpQVGxRZ1ZGSkJUbE5RUVZKRlRsUXVhbkJuWDBGTlRDMURiMjUyWlhKMExUSTVORmQ0TVRrMVNBfDZlMjc5NDZhNWM4NTI2ZWRkYTRkODMwNmM5NmFlZmVlODdjZDZlODllNmEyNTUwMzQ5N2VmNWRmYjMyN2QwNGE"
    row_4_image_1_name="Martell"
    row_4_image_1_description="Chanteloup XXO Martell, an exceptional blend of rare eaux-de-vie from Martell’s legendary cellars."

    row_4_image_2="/medias/2a.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3w3Njg2M3xpbWFnZS9qcGVnfGFHVTVMMmhoWlM4NU5USTVNalEwTlRneE9URTRMekpoTG1wd1oxOUJUVXd0UTI5dWRtVnlkQzB5T1RSWGVERTVOVWd8ZTdiZGQ4NjgwZDJhMjhlNjQ4YmVjODEyOGJlNjNlYTAzZjAwNGJiN2EwOWM1NWU3YjU2ZDQ5ZjljMGE2YzI4MQ"
    row_4_image_2_name="Forum Restaurant"
    row_4_image_2_description="A glimpse into the elegant dining experience at the Forum Restaurant, renowned for its exquisite culinary offerings."
   
    row_4_image_3="/medias/RGSH-Xmas-Dinner-Generic-2.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wxMTY4ODN8aW1hZ2UvanBlZ3xhR016TDJobE9DOHhNak01TlRNNU1qYzVORFkxTkM5U1IxTklJRmh0WVhNZ1JHbHVibVZ5SUVkbGJtVnlhV01nTWk1cWNHZGZRVTFNTFVOdmJuWmxjblF0TWprMFYzZ3hPVFZJfGFiN2MzOTZmNGYxOTljNTFmODBlYTRkNzYxYjdhODM3NjQ4ZTE5ZjFiYzEwYzcxMjU0Zjc4NGUyODc1NzEyMmQ"
    row_4_image_3_name="Regala Skycity Hotel"
    row_4_image_3_description="A festive dinner setting at Regala Skycity Hotel, capturing the warmth and joy of the holiday season."
    return render_template("home.html", 
        row_1_image_1="https://lifestyle-api.asiamiles.com/"+row_1_image_1,
        row_1_image_1_name=row_1_image_1_name,
        row_1_image_1_description=row_1_image_1_description,
        
        row_1_image_2="https://lifestyle-api.asiamiles.com/"+row_1_image_2,
        row_1_image_2_name=row_1_image_2_name,
        row_1_image_2_description=row_1_image_2_description,

        row_1_image_3="https://lifestyle-api.asiamiles.com/"+row_1_image_3,
        row_1_image_3_name=row_1_image_3_name,
        row_1_image_3_description=row_1_image_3_description,


        row_2_image_1="https://lifestyle-api.asiamiles.com/"+row_2_image_1,
        row_2_image_1_name=row_2_image_1_name,
        row_2_image_1_description=row_2_image_1_description,

        row_2_image_2="https://lifestyle-api.asiamiles.com/"+row_2_image_2,
        row_2_image_2_name=row_2_image_2_name,
        row_2_image_2_description=row_2_image_2_description,

        row_2_image_3="https://lifestyle-api.asiamiles.com/"+row_2_image_3,
        row_2_image_3_name=row_2_image_3_name,
        row_2_image_3_description=row_2_image_3_description,

        row_3_image_1="https://lifestyle-api.asiamiles.com/"+row_3_image_1,
        row_3_image_1_name=row_3_image_1_name,
        row_3_image_1_description=row_3_image_1_description,

        row_3_image_2="https://lifestyle-api.asiamiles.com/"+row_3_image_2,
        row_3_image_2_name=row_3_image_2_name,
        row_3_image_2_description=row_3_image_2_description,

        row_3_image_3="https://lifestyle-api.asiamiles.com/"+row_3_image_3,
        row_3_image_3_name=row_3_image_3_name,
        row_3_image_3_description=row_3_image_3_description,

        row_4_image_1="https://lifestyle-api.asiamiles.com/"+row_4_image_1,
        row_4_image_1_name=row_4_image_1_name,
        row_4_image_1_description=row_4_image_1_description,

        row_4_image_2="https://lifestyle-api.asiamiles.com/"+row_4_image_2,
        row_4_image_2_name=row_4_image_2_name,
        row_4_image_2_description=row_4_image_2_description,

        row_4_image_3="https://lifestyle-api.asiamiles.com/"+row_4_image_3,
        row_4_image_3_name=row_4_image_3_name,
        row_4_image_3_description=row_4_image_3_description,
    )
@views.route('/produce')
def produce():
    # This is a simplified version of your product data.
    # You would normally pull this data from a database or an API.
    products = [
        {
            'baseProduct': 'IPA_0054',
            'brandName': 'Imperial Patisserie',
            'img2ForPLP': '/medias/X-mas-Gift-Box-Mood-Shot.jpg',
            'description': 'Combo set includes Christmas Cookies (Green Tea).'
        },
        # Add more products here...
    ]

    return render_template('products.html', products=products)