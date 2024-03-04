```
# Make Application

$ pyinstaller.exe --onefile --noconsole  .\Chatbox\ChatboX.py
```

```
# Make Application with ico

$ pyinstaller.exe --onefile --noconsole --icon=gemini.ico .\Chatbox\Chatbox.py
```


```
$ pip install google-generativeai
```

```
import google.generativeai as genai

#API key (replace with your actual API key)
genai.configure(api_key="YOUR_API_KEY")

# Model setup
generation_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH" #BLOCK_NEVER
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
```


## ENG

* Get an API Key
* Create a Google Cloud Platform account.
* Create a project.
* Under the APIs & Services tab, select APIs & services.
* Click the New button and select Add API & service.
* On the Add API & service page, select Google AI and then select Gemini Pro.
* After selecting Gemini Pro, click the Add button.
* After the Gemini Pro API is added, select APIs & services under the APIs & Services page.
* Under the APIs & services page, select Gemini Pro and then select API Keys.
* On the API Keys page, click the Create New API Key button.
* On the Create New API Key page, select Read & write for API Key Type and then click the Create button.
* After the API Key is created, click the Show API Key button on the API Key page.
* On the API Key page, copy the API Key value.
* Using Your API Key in Your Code
  
* Import the "google.generativeai" module.
* When calling the "generate_content()" function, pass your API Key to the api_key parameter.

## TR

* API Key'i Alma
* Google Cloud Platform'da bir hesap oluşturun.
* Bir proje oluşturun.
* API ve Hizmetler sekmesinde API'ler ve hizmetler'i seçin.
* Yeni düğmesini tıklayın ve API ve hizmet ekle'yi seçin.
* API'ler ve hizmetler ekle sayfasında, Google AI'yı seçin ve ardından Gemini Pro'yu seçin.
* Gemini Pro'yu seçtikten sonra, Ekle düğmesini tıklayın.
* Gemini Pro API'si eklendikten sonra, API ve Hizmetler sayfasında API'ler ve hizmetler'i seçin.
* API'ler ve hizmetler sayfasında, Gemini Pro'yu seçin ve ardından API Anahtarları'nı seçin.
* API Anahtarları sayfasında, Yeni API Anahtarı Oluştur düğmesini tıklayın.
* Yeni API Anahtarı Oluştur sayfasında, API Anahtarı Türü için Okuma ve yazma'yı seçin ve ardından Oluştur düğmesini tıklayın.
* API Anahtarı oluşturulduktan sonra, API Anahtarı sayfasında API Anahtarını Göster düğmesini tıklayın.
* API Anahtarı sayfasında, API Anahtarı değerini kopyalayın.
* Kodunuzda API Key'i Kullanma

* "google.generativeai" modülünü içe aktarın.
* "generate_content()" işlevini çağırırken api_key parametresine API Key'inizi geçirin.

# V1.0

![example_chatbox](https://github.com/mrrsayarr/Used-gemini-pro-with-Python-GUI/assets/64076325/eb628e5e-880a-4ccd-93b5-e821d19cd5bc)

# V1.1

![image](https://github.com/mrrsayarr/Used-gemini-pro-with-Python-GUI/assets/64076325/d491680d-afaa-4951-9334-b89eef08a227)

* Red text canceled

# V1.2

![image](https://github.com/mrrsayarr/Used-gemini-pro-with-Python-GUI/assets/64076325/d25a373a-3179-4248-87f5-35b03f0f2a6e)

# V1.3

![image](https://github.com/mrrsayarr/Used-gemini-pro-with-Python-GUI/assets/64076325/245eeb24-8251-47bd-b356-8423336f94f7)

![image](https://github.com/mrrsayarr/Used-gemini-pro-with-Python-GUI/assets/64076325/05a0a404-8b84-49a1-8796-163935156314)

* Automatically saves Response text




