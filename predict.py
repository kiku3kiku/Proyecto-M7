import json
import os
import joblib

MODELO = joblib.load('modelo_sentimientos.pkl')
VECTORIZADOR = joblib.load('vectorizador_tfidf.pkl')

def handler(event, context):
    try:
        if event['httpMethod'] != 'POST':
            return {
                'statusCode': 405,
                'body': json.dumps({'error': 'Method Not Allowed'})
            }

        body_data = json.loads(event['body'])
        datos_entrada = body_data.get('features')

        # 1. Vectorizar los datos
        datos_vectorizados = VECTORIZADOR.transform(datos_entrada)
        
        # 2. Realizar la Predicción
        prediction = MODELO.predict(datos_vectorizados)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({"prediccion": prediction[0].item()})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Error en la predicción: {str(e)}'})
        }
