from django.shortcuts import render, redirect
from .forms import TestGeneratorForm
from .models import TestGenerator
import openai
import unit_test_generator.settings as env
import requests
import json


def payload1(context, model="gpt-4-1106-preview"):
    messages = [
        {
          "role": "system",
              "content": """
                Write test cases for the following Python code:\n
             """
        },
          {
            "role": "user",
            "content": context
        }

      ]
    

    
    payload = json.dumps({
      "messages": messages,
        "temperature":0,
        "model":model,
        "seed":123
    })
    return payload



def generate_test(request):
    if request.method == 'POST':
        form = TestGeneratorForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            secure_ai_url = "https://api.openai.com/v1/chat/completions"
            # Call OpenAI API to generate test cases
            api_key = env.OPENAI_API_KEY
            payload = payload1(code)
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer "+ api_key,
            }
            response = requests.request("POST", secure_ai_url, headers=headers, data=payload, timeout=10000, verify=False)

            print(response.text)
            generated_test = json.loads(response.text)['choices'][0]['message']['content']
            
            # Save the generated test case
            test_instance = TestGenerator.objects.create(code=code, generated_test=generated_test)
            print("Test Case Saved:", test_instance)
            return render(request, 'test_generator/generate_test.html', {'form': form, 'test': test_instance})
    else:
        form = TestGeneratorForm()

    return render(request, 'test_generator/generate_test.html', {'form': form})
