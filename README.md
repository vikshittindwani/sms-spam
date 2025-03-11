# SMS Spam Classifier

## Overview
This project is an **# SMS Spam Classifier** built using Jupyter Notebook for model development and Streamlit for an interactive web application. It helps classify SMS messages as **# Spam** or **# Ham (Not Spam)** using Natural Language Processing (NLP) and Machine Learning.

## Features
- **# Text Preprocessing:** Cleans and tokenizes SMS messages.
- **# Machine Learning Models:** Uses algorithms like Naïve Bayes, Logistic Regression, or LSTM for classification.
- **# Interactive UI with Streamlit:** Allows users to enter messages and get real-time predictions.
- **# Accuracy Metrics:** Displays precision, recall, and F1-score.
- **# Data Visualization:** Shows word clouds and spam vs. ham statistics.

## Installation
### Prerequisites
Ensure Python is installed. Install dependencies using:
```bash
pip install pandas numpy scikit-learn nltk streamlit wordcloud
```

### Clone the Repository
```bash
git clone https://github.com/vikshittindwani/sms-spam
cd sms-spam-classifier
```

## Usage
### 1. Model Development (Jupyter Notebook)
- Open `SMS_Spam_Classifier.ipynb` in Jupyter Notebook.
- Run the cells to preprocess data, train models, and evaluate performance.

### 2. Running the Streamlit App
To launch the web interface, run:
```bash
streamlit run app.py
```
Then open the **# localhost URL** in your browser.

## Project Structure
```
sms-spam-classifier/
│── data/                   # Dataset files (CSV, JSON, etc.)
│── notebooks/              # Jupyter Notebook for model development
│── app.py                  # Streamlit application
│── model.py                # Classification logic
│── requirements.txt        # Dependencies
│── README.md               # Documentation
```

## Dataset
The dataset used is the **# SMS Spam Collection** dataset, containing labeled SMS messages for spam detection.

## Screenshots
### NoteBook
![WordCloud]("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxITEhUTExQVFRUWGBsbGBgYGSIgHhogIB8fHx8fHRoeHSgiHSAlHR0gITEiJikrLi4uHh8zODMtNygtLisBCgoKDg0OGxAQGzImICYvLy0tLS8tLy8tLS0tLy8tLy8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAHwBlwMBEQACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAEBQADBgIBB//EAEwQAAIBAgQCBgUIBwUHAwUAAAECEQADBBIhMQVBBhMiUVJhFjJxgdMHIzRzkZKToRQzQrGys8EVYnLR8CRDU4Ki4fEXg8IlNURU4v/EABoBAAIDAQEAAAAAAAAAAAAAAAADAQIEBQb/xAA8EQACAgEDAgIHBgUCBgMAAAAAAQIRAwQSITFBE1EFImFxgaHwFDKRscHRBiMzQuFy8RU0NVJTghZi4v/aAAwDAQACEQMRAD8A+ccZ4s9tzq7Fmukk3bg2uuoACuBEAUAL/SN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQBPSN/CfxrvxKAJ6Rv4T+Nd+JQAQ3HG6oPDSXZf113YBT/xPOgAf0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAT0jfwn8a78SgCekb+E/jXfiUAaLoRxN7uJtmWWHjS5cIINq8dQzkbqKAM70p9dfbd/nXKAO+jWEs35sth77uTIuWDLKI2NtuyROsyp86xavJkxfzFNJeUun4rm/gy0UnwX8Y6MtZV2t3LN8W9XVSOsQTEugJAgkA5S0TUafXrI0pRcb6Nrh+5/ukQ4e0HucID4fCtaQm9fuXVgHfKVygDludaZ49Zcik/Vik/xspZRg+AYh+sKWw4ttlc51yqdd2mI0Ou1MeqxQrc+vK6k2iPwXEC8MP1B60iQsjUROYNMRGszFT9qw7PEvgncju9wa8mjWRJRnBzKQVXViGDQY7hrQtVhkuPNLv3IfPQrucLvBVmyAHtG6pkeoN29bTY6Hv2o+0Y3avo6+JVLnqB9VvEconfUT/StO3yGHjdkxC7f63qHwyGrCbWCZ1B+aEzEsoOhiYnyqrfYTLIouuQyxwNJbPdAyqpkRrmQPA110D6+Q76z5MsotJL6+qCOXcrS8/k6LX4IFcrbm6DZZpjT+6ynzNLWe1cuOS2/wAxZxHCMqWWKZQ6b9+p19uWKdjmm5K+jLJ8sbPweyLHqu12bBLToRdk5UWOQESec91V3y3ezn5GfxZb/Zz8hdjcItq5ct5esCuwDZo0GmwpijOSUk6HwluimwOwiFdTBzDWdgdzHOmpJrklt3wEth1AeNRlEFo3zD1Tz0qfV5SZW3xZVlXOJyxlE66TGvqg6zVZcE81we3ETKSAJ1jVu/f1ai/YQt19S/A4K0y/OXEXmO1r/hIiBPfy86ZGKrllMmSafqpnL4IyctsHXQq8iOUTrUOILIu7+RxawDFwmSWYwAG2jUzvyqkuOSzyqrT4CrfDwjIuay2dS2Zj2dGYdkjXWKU3fmR4tpunwL8doxUoqFSQQO8aHWe+rxXHUZF2rLH+jL9a/wDClWLBHB+E3LyuyC2Qoac0z2VLQI5tsO81nzaiGNpSvn9XXy7hts9x3CDbW6WKFrTopCk6ZhOgK6924gg6Gox6hTcUk6ab/D4/oTtopxeFRbVi4M3zgbMCR+y0dns6T5zVoTlKc4vtVfEDrieHt2bzoFZgMuXMdRKg6kATv3VbT5HPGpS6/wCSs074YM5UjS2Qe+SadaKJNPlmi6CdDGx7OWfqrNuM7RJk8gNthqTtXL9I+klpEklcn0Q6MbH79E+B6gcSOYc5Uj+ED86xLX+kurwcfH9ydsfM+d2bWZwoOhMAn/KvQxTbSFt0rLrdi2zQucqASZCg6e+AKuoxb4KttLkusYdVvMmjLkY6geDMO/X2VKilKvroVcm439dSnDKDauyBIykGNRJjeoj91lpfeQHSy4zvcOTMUVmkPlaQI2Jka+Rpzxq6QpTdWzy1w9XgozQZ3AkQVB59zTULGn0Bza6lGKweUhVkkgk+ySB+Qn31WcdpaM7VsvHDNoLQeUax9tFR8yniguIw5RjIMTAJFV4sbCaYWnBr5dbYs3C7LmC5TJXv9m+tR4mOrIebEld8E4lwi9YjrbL252LDQ++amOTHP7pMM2LJ91gNpZMQSSdAOdSnFdS1xXUa3ujWLRM7Ye4FGpMbD2TI0pazYm6sUtRhbqxdhcG91stpGdgJIUSYHOrTlFF5zjFW+A3A2Euvkt2bjmCQq6nbnrsDzqspbVbYmblFW5JFYwwdjaS1cN0mAoGoIJkROumm3KjckrfQnc16zaof/J4hXEhSIIugEHkRaxFSOTvkW9IEDXkBmC12Y3/XXO+h9CG6QdwDA57DW3xV21Ze86i0iyXZUzMW7QEBYEayT7a5uqybMqlGCckly30TdKuvcvHlAXEMElgqbF261u/ZJDFFGZZIdYz6QVj3HlBp2Gc81qcVcX0vpxafT2kSqI44Vxizbwlmw0w5vpcdQestK+XKwjkYkrrIBFJy6bLPNLIl02tLs2r+k+wptWKblxLWCxFjrFZjiLZXKdHQK/aHlJFP2ylnjkcaW1/B2i3VjT+0rJKWzcCi5w9bBuQSLbg5oaBMdnKYnRqT9nyq5bek3KvNV9P4BTJw3FWsOMLZa4t0C873HWSltGXqyAxAkQcxjajJiyZd+RRa4SXm2nf+CGy3iPEbHUYoI0sp6mwNdbR6oEjTaLZP/N51XFgzeJBtcfel7+f3+RFmLW+dSxJnT3d1dhTfccn5j/oLYwlzFEYsqEyErnaAWkRJkcp3rFrZZFC8fW/kIzuSj6gNxfD4QX7vU3H6sMcuUAgDyLOCf8opuHe4Ld17lU8lcpfXwBcXh0LA2gzLlQEyJnKJ01jX3CmKu4Qm0vX4fP5jjo9xDAWrbLisI91wxOYchpA9YVlz4s8pXjlSCcZydxY96d8LwtrCWb+HsKhuFTqJMMswQSRNZdJkyTyOE5dBeCcnNqTKOE27yYe2ts4xkZQwNs2wuupC5xmABJE6TqRoa0Spyd18xORxc23V/H9DM4HCKuKJe01y1buAOjMuYyYAOokz3U3JJ7KTps2W3Dh8s3/RWxwrHM628HkKAE5uc90Me6ubqJajCk3PqZsjy4+sjBYxcGrOjG/IdwQhXKIYwBm12iulHe0nwaE8r6UB47D2ixNtsqkDKG3P2bH2gCtEY+qrfJaLlXIz4BxK5cuZGIICzsPKtumzSlKmTJC/DY0W84l1YuTKgHTuMms26mymTG5Nd/eCYm+2dtTvzAn31Rydl4JbUHWlNlLWIBJcsdDtEEfmKvkxLwlJ9yJRUk4svt8UVTK5FATKFGcaZs3rZs0zvrrSPDT7iXjk+t/L3CviFxmYuywXJfTbtGdKsqpI0QpRpduDt/oy/Wv/AApQWLuEcYu2AVthTme25zDnbOYc9p37xSM2mjma3eTX4lk2gg8Tc27qNYtHrmLM/azTqREPl0kxp7ZqVoqlGVvjhLivy7+8n3orv8SzW7Vs2LUWzoRnk6ywb5yIY7wB5RUx0tTlNSfPu/bsFryPOJY5r1wXOqS20Qck6wI1DM3IRV8Gm8KO22/fX6JA0pdUHdHuF43HO6WCvY1bMVUAHTu/dWbV6vDpUnk7/EUsMX0R9Y6PdFcRZ4bicM72zevdZDKTlGZAok5Z0jkK8pq9fiy6yGZJ7Y17+HfmPjDbGkfO+J/JfjLFm5ee5hyttC5Cu0kASYm2Na7uH03gy5IwUZW3XRfuVcGZvjKLbdMgymATE6HyJAkab6114N9TNibknY7x/RDH27thB1d18ShZRb8OhOfMqgbjU1ix+l8M4zm3Sjw7S+VXY7w+xoLfyWY7V/0jD9YRBBk8oicndptWF/xJiUr2uvPgnwVVHz/FZrLXbJIlWZWgAglTGhjaRXdxZVPGpLurKuKsZdF+huLx2tpQLYMG45hR5cyT7Aawaz0jg0vE3z5LqWUWzTcQ+S/HKrPbvWrzTmKqYJI7pETrzIrHj/iHDKVTTj7f9g8LgyfWqhyXRdF0ZlZFAGWSZERzH511/FyT9aDVdviLcaPeEcOxOLxBXDIztEdogZVGks2gH+t6pqNXDBDfmf17CVBNUbVvkwxsfSMP1kerL/ZMf0rkf/IcF/cdefH7lvARgukGAxFi4bWJQo4jfWRG4aSCPZXYwanHnhvxu0QobTZ9OeM3LFrDJZY22e2C7roxAjKJ3iSTSMEFJuzm6XFGcpOXNMG6PcQuYnAY1L7G4LaZlLakGGO++4q84qGSLjwXywjjzQceLYN0Hti1YxWNgM9pctueRO5/MfnU6h7pKHmX1b3Tjj7PqJ8J0uxiXRcN+40EEqToROojYT5Ux4YNVQ2WlxONUa+9ZXDcXsPbAVMSvaHm0gx7SAftrOm5YWn2MSbyaaSf9ou6O2/0JsdeIjqXW0p9r6x/yx9tWyPxFFefI3M/GUI+fPyDcHhBZ4rib0di3ae8D/iUH+rfZVXLdiS+BSUnPTxj3boUfJ9cLYkMdzeBPvtYiti4OklSoW9IDF5NQO1d1Ow+eub0S6EtWNsLw4ogupxHDqiXg47Lx1kcgUk9ncbQRNcnJm3y2Swttqu3T8fPoXUaXUD6WXLgu2yz2LoNr5s2lyWghLAhVKgetmmOc1q9G7FCSjFp3zudu6XX4dCmRX1E+HxTzOmmgiBH5bQa6K3MW8Ka4CeAcJ/TMT1LXBbYgwSM05RtuOQ38qzanK8UXKrIm/DjdHPFLIw927YcZmtsVDDQHlOWO7zq0Ms8kVKLpP2DIz3JMecY6G3sNg1xHWhgApKBNVDxPanWD5Vmxa5TyeHXmZ45YynVAHRXg93G3mti4LeVMxbLIjQAQCNwadqdV4Md1E5JRhG6FaWct/qRcAXrcnWEaRmjNE7c96YsslDcl2uh1+rZs7PybrdPYx1p/wDCoP7nrBP0i1zKDX17jO9S11iZTH4RMNdvWmti6bbZc8so58gef9K2Y5+JFS6WMuU6adWU464zOvVqUDIkIJGyAT5g7g8waYkRBJRe7mm+fieYjhjKjOSWO+ncTufPyom9rS8y2PIp8Lsb/p2k8MwYgnS3sJP6uuVo6+0Tv2/mZ8LrJIxz40OEzYPrCqKocm5JAEDZo2rouNPiX5DdlXUq/AI4dhzbu4lCMuVgrBC5CjtTlIUkkaRPnScrtRf7E7t0UzRfI6oF3EgEMMqaiYOp7wDWX0l92PxFarojMXld7t0W8NbfLcfMzTqczHfMBty8q2xpRVvshnCSuQJxPMboLIqEEAgH1IMERmrTFeqiY1t4YRwUf7U8R6vL/lrVpf6j9xaP3ECJdcBvnAihyJ1knu0B0pLb55KyjHd0tnAxJRmuEW7mY8x+cHapjLb63DGRVKhzjMflsW3yoc0aEaDTlWyeWscZUCXIl4hjjcUDIogz2VismTI5rp8i+ygbGH1f8C1nRSHctf6Mv1r/AMKVJcFtrPMD2mpQWMrxsFSFL5h6pJEf63pa8a1bVBYNZRgw6zMgIzTGpBmCJ9YGreI2ntdg5UFXkt5RlckzzgaHf7e7yFCnlfWividit7Nlc3zjAxpEa/ZS34lq0gTs+k9CmP8AYONMmfn/AOWtec1//VMX/r+bHR+6z5hdssAe2TA138v869Y8VFGgjjttg2o0ErOQqO/9ry1gaUiAjC1R9d+UDizYfA4bq26u5dVLfWjRlQqC2VtxJC15P0Tpo59VNT5im3Xa74v5mnJJxjaPkuHukN1i3mS7Jl+s1OviHOK9c8WOUdrSry7GZzmn0KLmGDsqo2e49wrJbeYg9+pJ1om4wjfZFoSk3yfXunPCcamEw+C4fafqwvzhtkDbkdR6xJY15D0dqNPLPPPqZK+1/XboaZJ1SMd0V6M8XwuJt3UsXVXMucZhDLOoYZtdCa6us1uh1GGUJTT4469fwKpNMN+W7ALbxNm8mjXUOaOZQgA+2CB7qV/D2aUsMoP+18fEMiQ96N8Pv2OC58GjNisR2pESJaJknkg+0zWLV5seX0jWd+pH6/MlKo8GFToZxcXOtFi8LkznzjNPfmzTNdl+ktC47HNV5Vx+RXazbfKfg3ucKw9++mXEWygeYkFhDDTkWg1yPRGSMNbPHjdwd18Ony4LS6GT+UVdcJP/AAK9HpVbfvOdof7vecdCPofEfqv/AIvUZv6kPeGp/q4/f+xX0HxaOmIwdxwgvr2Cds20e/T7KnUJ2prsTq4tSjlS6fkU4XoFizdy3ECWwe1czDLl5ke7yoeohVomWtx7bT58jrpjx1bmMV7JBXDhQjD9oqZke/T3VODFUGpdw02FxxNS7jr5RfmrJUH6Tf632qEQfxa0nT8y9yM+j9aV/wDaq+ZZjsV/9NbFDU3sPasH2qzqx+w/lRFfzdvk2yIx/nrH5NsSfJx9IX60fycRW06gt6SpNxRpvd3+uuUEN0dYDGGzZVL+FS/YuOz28xZe0vZYo6MCRsCDI0FYsuHxcm7HNxklTqnx1Vpr8CykjjF8Tu37qJaQW8qdVatWwdATmiWJZiWMkk1eGmx4otzlfNtvz+HC4ByXUCQOGYNIfMQ0zoecwdwe+t2Gtq2gmG9Gb/UYyxdJkdYASP72h/Jqz6rG5YpL68xeVboNGi6Z8JzcYtoonrjbY/bDH7FJrFpstaVt9rEYp1ivyNVjcR+kvxLCA6i2mQcpy/0aKxxj4ax5H5iUtqhIzvybsLeHxmLOmVAo9yz++K1a715wxoZnVuMTC2HKjR1BmfP/AF/2rqrjoaJc9Ua75J7pbHNOsWGH/Ulc/wBJO8S9/wC4nUpKHHmDcdF1sZjEti2QbwnOqmPW71OgAJPdFN09eFH3FfUUYuV9OzEPGM4yh2DHcFQIIgZcug0yxArSug3Dt5cV9dwnG4fLaciBO8SdSRInKIH/AHqMi9aPxIwz3N39fNm36c32ThmEKMVOVBIMaG3BHvFcnSJPUTv2/mKwpPJKzD4rjWLDKpuXLZCWwqqxChci5dJ5rB99dNY8dXQ6OLG1dX1/MY9W5e/duZUd3zdXIlSCwJ7VttQdojc0iTXEV9fNERpRSXQefI0pF3Eg6dlP3ms3pP7sfiU1fRGXv3LqNedQroMS0oQTJIcaxrBBI3rbGnFL2DKi6T8up5xAMCc4VTIMLoBtsCCZXQGTtWqH9NER5XB7wT6Sx3lN/u91aNN/U+BdKoI5tXbmQlb6p2yMrHYfdOtLt+Yqajv5jf17wLEgOG7WYgk5tNdzMDXWqSaodHhLgPx7RhsOe4r+6tGX+jEKu0UYhrXzjMq5jMQ3m3cSZ1X7KyKaYpRyKkn9cf5AuIqgKhRBiW15nl7BQxmJydt/A9f6Mv1r/wAKVA0DAoA13SWyrWDfs2rdu0t1VyNZyXUOUwpbUXFMEkkk7bVytJJrJ4eSTcmm7UrT58uzLvpZ30luNcbBq4RbT2MPnuC0gyzo0OF0A10mPKo0iUFlcbclKVK3+Vg+x3xDBqf0tWw6WksOosuEIJ+cChCf95nSWkz6s6DSq4sjXhtTbck9yv2Xfsp8A11COkfD7Y/tBDh7dpMOVNl1WDJcCM37YZSTBmI0iqaXLL+S1Ntyvcr9l9O1MlrqPOhP/wBgxv8A7/8ALWsfpD/qmL/1/NhH7rPml5CRlEkaR2x+6vXT4VdveVlwhnxG6+aHDQbTQGAnY7kHzP8AlWBrhV5ozYFHlo2/ywfQ8D7B/AK4PoP+vl+u7Nc+iPneEwRyq2dQGmdAYIz6aneFB/5hXpN1GSc1bVfXH7/IowuPKXEfcI6tEATlM8qjJHfBx81Q2MUnZ9e+U/jGMt2cPisJeZLLjt5IOrQVJ0OkSPsryfofT6ec54c8bkul+zqPk31R8/HT3Hf/ALV//p/yr0H/AArR/wDjQndkFXGeOX8UFOJuXLjKDkzRAmJ5c4rRg02HAn4UavyBuTZ9SwGPvvwFHwbst6wAGCansntCIP7JzV5nJixw9JuOderLz9vT58Dv7eDAp09x8a4u9Pll/wAq73/CtF/40Kcp9gbifSnE4i2bd6/euWyRocsSNuVNw6HS4Z7scaZDc2gHBYQXesY3Mi2lBlhOhYLHt1rVdPgTPI8e1JW2WYLA9a7JauEoqFmOSDA0gKCZMmBrQ35kZMuyKcly3XX9Qm3wNy1pQ8Jdzwz28pUoCSGU+Uagneje0LeqSjJ1yq6Pz9pRjc5sZ0vvcthsjKQRlJEjSSIIB+yov2fIZCS37ZRp9S3jV0vZw7tGZrbyQAJi5A2A5VMO5XTrbPJFdLX5FdzhLdYyG5NtbfWC4RoViRAnmezvvQpcErU+omly3Ve0FtWZUS6gHkXA/KNKq8qT6P8AA08mg+TxYxIG8XRt9ViKnqAFxiwlzEW0e4LSlrsuwJC/O3NwNd9PfVcknGLcVb8iGazH9FbT4TB2xj8Mot9cVctpczOCcuv7Oxrj4tXOObJLw5O648qQndy7QFw3othrF5MRc4lhmW0yuQjAscuoA15xFNy6vNlg4RxPnjnpyTu4pIyPE8Uty9euqTFy5cdRroGJPdvrXWwR2Yoxb5SS+Q6PCoGxVoJ1ZXQlQ0+dDFwk5N2fYLeHF/GYLGx2f0V3PloPiH7K4LlsxTxf/b6/IxXthKHtMd0G4uG4s7mSMQbgHvOYfuit2rxVpkvKjRmh/KryG3EsGuD4XetE5euxLqDHIPGw/uJ+dJxyeXURl5L9P3YuMt+RPyRi1xGGELlRh2JYgg6RmPqnefy84rY8eV87vP8Ax37Gzd7DW/J5fRsecuTSy/q8hNuBMCY1rHq4OOHl91+pn1Mrh07ma6V3GGNxQW4VDOwYAxI7j310dJBPDDnsNxY4yhFsTXtSM75gNPOANP6CtDgl3GbFFeqWcQuowGUREnYDTSBodeetEkKx45R+8z6J04eOG4IwrR1WjbHsbHyrjaRXnn8fzM2LmcviZPiPH1zBhhsK0Kg1ViZVQvjiAV08oroLC0vvMvjxOq3MV4m9dZmdrh7bSdYBOrd8b09YYo0RjFcLsbn5IP1uIObMSiEn3tXL9KJKMaM+r6IxWJxNy1iLzW3Kku40Yg+se4+VdHHBOEbp8IfsUopM5w2Da4QxyEEy3zgDEc5kz51ohC66fiQ5qPn+AytG1ZIZbcljlBFxW399aFOGL1kvnZG+/wDYExNm0c8WLmYEiQ0jN7jrqRtSJTwvoiVkXHIFew10KFjYFiOY1Ya6+RpO61RKyRYy4cWe31Nyy7BZgjlEzuRqIO3ce6m/asUYKOXoSvWfqlWO4enZFq1cJIDSJOhUsN/7oJ07jSp6jTterxz3/D8y1SFWLwrW2hlZeYn/AF36VSM4zVxZPPcuf6Mv1r/wpVgB7NsEMZ1Gw7//ABUpWirdMY8QvPcUdZiHu5dFDPmjQ97GAYG3eKrDT4sduCS9ySI3yb6HjO5Q2uucWVghS8rPflmKnwMe9zpX59yN7o8v4lyoD3Lji0y5FZ5AGs5RJjYbeVV8DHHc4pJv3cllJtoY8Uxd3FXC/a6tnLi21wEJmmIBIA+wfnStLiw4IRjStKm65dFnljfIw4b0r/RMBfwDWcxvZ4uBxAzqF9WDtG01hz+j/H1UdQpVtrivJ35kxmmuDL3nXKY7tFyxl21n/W9duTVP8q6EsuuMQzMLRQFWUjlMakaaRI0rPLE2lfn+QmEkuLs0/SzpY2LTD2VsMjWVBPamRlGvqiNp51g9H+jZaTLOe693squb9paeSMo8mVuYgKSHt6jkeU+0e/7a6u7zRRK1aZW6qxlotCBGh189BS5yfZFlx7TW9D+nT4S31FzJfsGewwMrPIHKRB3ywd+VcfXeioaiXiR9WXmvpfiMU2uw7t9MOE5wLXDbRfkSqgT5HIT+VZ4eiddk4eofzJeRJXRjOk/F/wBMxPX3FW0sKuW2ZIAGm8SfcK6uk0n2XF4cXb82Uc9z4CejfSs8Pcthyzq0Zrdz1W89PVbuP76Vq9BDVxrJw10a6r/BMZSRpr3TnhbMTc4Zba4TqRkIJ78xUT7SK5z9E6zH6sdQ6Xv/AHLqafNGf6bdJf0tLdu3h7WHtWpYKrqTrA2WAPZE1s9H6L7PKUpTcpPu0yHKxTgcHdFq6qqGF22muYDL2ww9aJPZjTvFb3mgnyInDdKMvL9qLOE2L1lz2Q2dGDKHgx2dm2DAx386h5oMjNiWRL2O0MMCpGKsHI4UrcIz3RczdhtQVgAfvq0ckZ3TM2aDjhldduiruhRfxam2LVu06Wy4d5bMWgQADlAAAJjQ70ymOjBqW+Uk3VL2fMs4hi7T2URLV5TbVgpLAiC2Y5gEHfyipSaK4ozjNyclz14/yEY669vCJZdYvOcuU+sLanMoI5S5MeQqErZTHGM8znF+qvwvv8hc3CmCFyHAA2yGZ8+QXnm/rTfDdWPWZOW1V+P1z7B78nH0hfrR/JxFLHizpKYuL7bv865Up0yUeOMQbGGDqTZHXGzlAJ1YB5A1jMBvWeEsayzafPF/hwLl3oGwku6pZDs7EBVyjXQj+tPllUFuk6SK7f8AuDOM8ExeFWb9p7auTB7JEneSsxS8OtxZbWOVjIzXRArWi+WcubIMqGZjeZiJO8GtKxt+/wAiihVm04T0uVOHrhyD1xtOltuWsgeY5e8CudL0bKeVT3KnzXN/kJlgbnu7GP4Gz27tm9IGRwVBB1g6jQad0mt08DywcW6vgfKKaaNF046ULjEW3at3LYtOzNmgawRAyk95+2sOk0U8MpOXuE4cOy7M9wNrS3s2LtPdtqplVOvlrI8+dac2PK41DhjZRdepwbbg3SLh1i6P0fBXluOsCCpJB153I5VhyaHVT9Wcl9fAzZcc9tzlwdXcRgMSzXW4deZmY5mLBZPP/eD8qvj0WsSqMlX17BbyOHG9fXwMJxixbS64Nu7bBLFFJGin1ROsxz1Na9uWKSkbceRTjadmk6PXuGvbRTgbt26qjrGDaE8zrcAEms0sGqnJ7JcfXsEZpSg7cqRoeN9IMIbKpiMFeNpICiVIWBA1W53aa0n/AIfqcbclJc/XkIxetL1JcmN6RXcDdsB8JhrlrLchnZpEQdIznWSDtWrBizxd5JWjVjclPbOQP0Yt2F6y7ibFy9ZAgZTENI1PaHI/nTM+PLKN4nROWfrKMXTNhwPpXw+wty5h8HeQCA7Ar7t3/dWCei1GVXKSdfXkIyQk2oyl7gR+J8GuDrHwjjMTMtBJ57XO+pWLVLhT+vwLVmXCZjxbUXm6tQ6OXAQHULy15QO/uNdPDfRq+Bzdx54o6azI6u2pQB5LOZOYDbTTQSfdTXG1tSIvu+ToreU7oDmnbbMQD+Y1FU8JlagzwXrjJ2SIYlIAiZ7h552302qsopR3EqEd1fX1wHW8RfW7iE6ot1Vv5xSwBVU0YmNDLNJy6/nWHK8eSMJbqt8cdW/9u47DDYmg3DWMUyB1s3AvUr2syKCizkKydTo0xrHtrLOeFS2uSu32b5fX66DlZl+KY5r1xnYnUnczuZ/ea6WHEscFFFG7Z6/0ZfrX/hSmkAVAD3o7wjrOsa4jZVQ5ZBEtyjv2puOF3Zj1OfZSi+4CcNcAnLe0/ukCKr+I9Tg31RQ1waEz79efmaLiOVBmDw15xNtLhAG4mPdr31Kin0QqeXFH7zQBcVg0OCCOTf8AeqJUy8Wn0LmZ2DME0/aIX36mrubd8EuaTpsuucQUplg6qomeYPaPvEUOfFCVjad+8txF4JqEuAG0UGYROkAihtL8CsVu4tdb4POH4Q371sZWy9kMYMQoE6+cURW6SDLkWKDd88lnHMAwulbdt8q6CFP741onHngrp8q2XJ8+8p4ejBLmRfnQQIIkgazAPOYq2NOnXUbJptX0PMElw4hSynMGGaBt7QNqIKTyckya2cHuAssLjnUFVJjKCx1GwYfnRCL3MJNUizigYXLbIDnKAnQEzJGoAiY8qnImpJrqRCqdlt1CuIvHLHZcrI00HKdKs1U5P3kJ3BfA84nBUzAAdNgP2kLHbvOtRk6fFfkELv68wBr8LC3WOggaxSKiun5DE5eQVgCrLL4hkOoiTtTceLE1cmk/cTbOuK4JrWTK7PmkCeW2321bNiWJJruCkV4vht+2pYlT1cK4W4CUO0MAdNRFYo54yaS79OOpWovsV4FFcHrLxTkJ1kVrxxhL70qJ2pdEX8R4UFQOrl55nuiZn3VfLgUIqUXZF0c22Tqzm6r1DEM2aY00mJn3UriuRTUt3F9fZQ6+Tj6Qv1o/k4ilmgV9KfXX23f51ygDS/2vjcPw/AjBlwrC6XZUzHN1jdk6GPZzrk+DhyajJ4vsq32rqKpOTseYXhN0cUTEdSVz4U3HIHZW6UKkTyO2m+tZZZovSvHu6Spe1WVbW2jKdE3a7g+I23ZmXqluCST2w0iPMn7a6GpSjmxOK5uvgXnSaYjRyCGNtusRQPLuBIidB+6ussi4lXKJ3x8zy7bdbiDIx6nQwN4YmR7dfsqN/MfYVjli4p31PUvdkB8yiSVhsp1OsyNdedWWRNU/ky+5diYfB3WR3TKVVoknWTG32ioipU2ikssYyUWUMHJPq6ax7JH5yahtl9yGHA7bDFWs0SCRp/g0nltVoXvVmfUyvFL67k6Trda4XJJXMQoHKP8AwTScmW8jXkTpoxWNIu4+5fCYZ21bUT7v+1OycwixWnW3NOK6FuN+bwdhEIXrO03LNtoft+wUSe3GqIh62eTfNcFfRZz1vVkqUuKwKAyNp25d1Rhlcq7E6tLZuS5Xc5wVsdTjLPgOYf8AKSP6CpivVlEmbe/HPz/UP4cQtuzh/wDi2bjH2tqPyBq8eij5oTk5lLJ5NCyAmBhpBuXTPf2f+4pfTH8R/MtRa7L8wjoDgMNexgt4i61q0VYzmyZmGwLcuZ91cv0lmz4cDngVu12v5G6EIyfrlHGbdu3jb1qyz3rIZkQgyxHkY1gjfnFadDkyTxRllXrNcoXkhGP3eAPieIBDKquJeWLd8ERp5E1ryS7JdymOPdvsU8PtI162lxyqNcUOZ2BIDN7hWfM5RxycOWk6XtHKKs0/TjhGEwuKtDAu11Qoe4ocPlgz6wEagTXM9G59TqMMvHVPouK+RbLsg1TCL93Di5j764gP+kWbi20CPmBZkaGlYUiI31pcMedww43ja2SVu1XCa4Ic4q+eoo4vxMMuERLh+bw6qwA2bOxI15wQfsrZptPUsjmusrXtVIrOXCoz+JtwecneRW5pLoVjKy9/oy/Wv/ClQWB8KQGBLFY1BHI8qlFZ3XQ2fRziNy4l8tcL5QMp7tD5VoxybTOVqcUIyhSqxPc48TKm5fKkRHZmD7u6sniZ2uqOitNgTtRKeC4S3fxCIM3VrJIbcgGY079KZhjKTqRXVZPDxuUeox4tjMabjC0txLamFCryHPamzlO+DLhx6dQW9pv3l3ErL3sGLl5SLts7kQSJ7vMfuqzTlC31Iwyjj1G2D9ViTgPE+ocMZKPIceXf7RNKhPazVqcPixpdV0HK9HraXjeJH6OozjXfy8x+/QUzwkpX2Mr1cpY9i+/0FPE8U2Kc3D6gOVRIED/PnSpz3Pk04YRwx29+4w6P4+8MRbsF2yiRlMRAUkbCmY5u0hOpxY3ieRLnzB+MccxCX7irdYKGIA00/KonkkpNWXwabFLHFuPYVXe1bNw6sbhluZkT++kt2zSuJbV0oJ4Pg7rSyhQp5t/Qc6fiwznyugTipdQ67wp2IPWWyROkd4jvpv2VvpJEKCQlxOIbVDGjcv6HurI+HRaONJ2GYLhFxlDFlVTqCda0Y8E5K7pFt1Ft/gbkSrq8chpVpaaTVp2G7zBsLiLagDqgzA9ot/iB7+4R7zXPljnJvkDnHXkKjLaCMQJOvvgTpJ/KKmOOcX6zAe8Qwhuvh7YbKSTrE7AHbmdNq3ekJ7MakVTpMsxuIui1duZQssucXsKqdYSTqDJzEHUg981xccIOcY351Um6ISV0ZQWp5iumo+0bQ+xn0a1/h/8Aia1Zf6MfrsKYk/QrmXPGkTuJjvyzMecVk2urJ8SN0af5OP16/Wj+TiKqXFfScfOL7bv865QAdwHjt/CqVs4vIhI7OVT3yQGJy/1mkZtHhzO5qzNKUn/YCnjWJVmK4u4WZw57UBmBmTLRpA5dw2olpsNfdXHHQvG31jQZxbphfu2zaFqxaBIa61pQOsIMgkg9+ulK0+ijCXiW3XS+xbwkxKMe7dhBJaRtrrM7HzNbuvCKvDBcjk8LxjSzG2GfcSQecer3AkU3wJmVZMMaSukJrmHuBmS4IZVZtRPnproPOkTuDpo1x2tbojLhJ/2HEf4v6LWnH/SkIy/14i7DozuqKiOx9/vP+dKSbdIbJpJttoP4Za6vGW1bICCZymY7J0Jq8VtyJMVle7C2r+mc9IcXLdmZVnGwiCTt3771mljfiSb6NjMC9Re5FnEgGweGGZRqdz7e6tE/6cROO1nm6OrEYrDpaDKt2ydM2zDyP+tqlevFR7oHeDI51w/kW8Owf6ITevOkhSERTJJNWjHw/WkVy5ftC2QXvYH0evK145v96rhu7XUeznS8bW7nuM1EWocdqLOIY3LjkKxltlEBG0c/3mrSlWT3EY8d6dp97ZOlhCm3aUzlzuY/vMTRl4pInR27m/YvwRq+HfJxhr7ZLPFrNxyJyrbBPnp1s15rL6c1GJbp6dpebf8A+TqLHfSRkOK4D9Dxd3Dm4Xy5kzqsH25Z/Kdq7ek1HjY45Wq3L8DLkTba8mDcUvLBCZjmfOSViNCAB371pyNdvOxeNPq/I1PAuiWGxNq2W4pYtXLg/UlFzKSYy63AST7OdcPU+lNRhnKKwNxXftXn0NUcMXzuKukHRD+z8QqHEq+dCZNuOcRkJadt5FO9HekPtsHPbVOut/oZtZHZSq/kZmxhblw3SpYgSdDuZHs5V1IQcroPVSVoicPcAm4cmojMdDuT393dRKEowbZO5dgXiCqHhQAIGxJGonnrzpMbrktG65LH+jL9a/8AClWLAYFAGq6Ga28QvMqNPcafh6M52u+9BiBeI3AIkQBGw5aVm2o3bIjTovj/APagXiWUrtGukbeynYKjIzazHeF125PeNcRxdm8yG44Ekr5jlGlWnOcXVkYMWHJBOgd+NXXtlXzsDoTm0+yKVuyN/e49xohgxRkqXIHwvANfuC2vtJ7hzNWjFydBmyrFFyZq2x2HdjgdreUKrT+0P+8e00/dF+oc3wssV4/frXsMzeD4dnsuJgzvHsII8qy5INOrOljcMqU0HdHbqHE2oWGky2Ymey3fVsMWsiblYvWL+Q6AOkSkYm7IjtE1OT7zLaZ3ij7ii3blAJbV4A5T5+dUSt0Mv1hzxy6UyWU0XLJ8xtH5TW/US21BdCY+YgZoY5ZEdxrE3T4LHSxkJI1zb1BXncEWMLduAZVYqPPT86bGE5rhcFm0NuD8Pu23kgBSNe1P5e2tWDFOErZVtAuLwLtdfJbY5mMQYmPL21h1GaEMkk2TTfQrfhN4pmNtlAE5mOmilvtIG1IeqxPi+fpE7ZDbiNpGewtxginN2iYAOXs68u1Fb/SDksacVf0ii6FPFbtjqypfrblpbZD9azB2b1wAdIXvA5azNcrBuU91cO+KqvIimZ66ynYR762Oi6T7j3Gz+jWo7v8A4mtmX+jH67FH1AZfaFzdVOfX1cm3dMaTFZufkU469r6e2x38nH69frR/JxFLHivpP+sX23f51ygAfFXcoYSNQMqgaj26d1apy2pr8BjdHMwyIACpAnT1p3P+u6o6SUV0DukTDPlF0A6LtEd9EHtUkuxFtJ0NeiiA3Lt3fKuk95/7CpwctyZg1cm0ovuJcTdLOWcuXOsyKQ7bt9TRGLSpdB5j7xfB27zauJSfIyv9AablW/EpMzY1szSguhfg8KWw+ItoupcAD3L/AOarprlhZGaSjmi35FGN/wBithLYOe4O1d/otMl/KVLv3Jx/z5bpdF2EluwGts0HMJMmYPsO0+RpKinFs1N06CGwdrsiTqV7UGDO+u32VfZHgjcwbGWUUrEifW0OmvKddqXkSXQtFtn0rj+Lx1jFWbGBtf7Llt9WEthkuA7lmg6zM6jvry+mx6bLhlk1EvX5u3TXuGCf5RL36RxNcKjrkDogyqBkZ8oYSAM0GtfoyPg6R5pLmm+vVLoQ+pd0n6T3cBiDg8Gtu1ZsZQewCbhygkuTvqappNDDV4fGz25S9vTnsDdAvS/BWsuFxiAWVxVss6KYVbgiSB3Gdh3Vq9GZZKWTTyd7Hw/YxeVcWkZezhbbZRn7TTJGw0mTzgHQ11kkKeScbdcI1HyPR/aiRtkuR7Irienv+TfvX5mzT3uVlPTO4BxXFHPk1cZoJgn2Ct/oh1pcf+kz5U3KXHcR3lZ//wAgvl7UQ2nKRI13j31vlb/uv8SlqP8Ab+Rfw3DRisM2aT1trMPMv392lZNYv5E/9L/Jl8M7lVG7+WVyuMtEMq/MftTr29tK4f8ADn9CXv8A0Ha1W0qs+Z2lL3LkOFUhizRpE92+8V6TGm31EriK4PbSorKUuktIHqldDoe1OmhqMijt638CXbXKPONfrmEzGUTmzbKBvzpWP7oY/unj/Rl+tf8AhSrlwexfKzEakb+VWjJoBhw7EXrRF63lGhEE+sBvpOsb1ZSa5RnzLHk9SQ0xHGLrHq2t2Qz9kxvr5zoTOk1Z5G+KM0cEEt6k6RnreFYhmBHZ3113/fSqNryJNJ9x+3HcVZUC6iONgW1MjcEg703xZLqY1psORtwbQVwc3eI3BZcdXaAZyUXwjQSZG9ZtVqnCBbwoaf11y/aKsLibuHtuFR1zes5Qgjlo3KnRyxSpMbkxRyyTk+nYWdV2c6h9D60aA+2qtx6LqPvsw7G8RbEhFZczqN1XtHvnXXvq88ia9YVjwxxW0+ovt5lcZM2YHu1BHlVLS5Q2STVPobbjeLxFkWPmRcd7KuxKHskzpp3RVcWt33dcOjnQ02N3UmlfmZC/iTrmUq/WZyIiPKNxUqXO43xhVV0qhrxu1myXlBZY1j8j+db9Qt1ZF0LJiNSCTCkzyiax9WSdqwy5Tp2xI7vdUexla9axz0jvMgRElUg7furbqpOKSjwiYg3Ry07XM5nKoOp7+6l6WLc7CR7iMay37i5iFk6CBrHOd/fWXU4oyyttA3JLg4xPEyEKLcuEEbEgjaDMf3dPtpHgQu6IjKb6jHjF5ENhnQXEBOZSYkQOYro65NwSTpkroKr+Nt3FYCzYtRqCA+Y+QliK5qhKLXLf4Epe0pxZXLINuTGiqQRp3mphuvm/iWYx4k8YWz7h/wBJrp5v6MfrsLq2KbN24VNsOQu8E6Vj3OqBqKe6uTTfJz9IX60fycRUFxb0lIF1CdRmuyP/AHrlSuvIIDfFAhu0zAgwuXbu+ytDyLnm/YMcl5ja9wq2qAJiJJ5SviAPPTsy3urDHU5Fx2Msc0+lA9vC2rTND5hkuQwI3EwAO/SiOWfVcEqc+3B3wHFrbxFy2zSryoY84MA92orZgyc+t3FamMpwUl1QJf6PYhXyqpYTow2j+lQ8M06RaOqx1d0F8ecWrFvDAgsO08ctzH2n8qtle2KgLwJzyPJ+AVhb/wDsuJdCR2tDsdlquC44GRlV54pgnBsat1P0W8dD+rbuPIf5fZVsclJbJfAtmg4S8SHxAcYj27gt3FXskHRQMw9vPSkeFskOjJZIXEsfEWe0QkAiB2RAJmNeXIz7alilDIqTfzOL9nrHS1aSXfLlCgas24B5gEwOWlVnOMIuUuEuRmFPqz6FxtsOgtWP7RuYI2rSo9i1mZQ2paWUiSSdZrzenWWW7J4KnbtSdJ124aZoMbxzgzcPvYe8lxb1t4u2bgEBspB1E6ax9tdXT6havHOEo7WuGvKyOg/4/wALTiF44rDYuwi3gpu27tzI1tgAp7P7Q0mayaXUZNHj8DJjk66OKtNENLqBdKeKYZmw2FRhcw+Ftles1hnPrMANwIEd+tM0eDLFTzSVSm7ryXZA35Ce1dwaskAlSFDmWBMlM+g8sxGp5Vs/n0/P4e2v0sq1fU1vyX3LH9o2Vs8luk6Gdba+sT/eDbaRFcr0yp/ZJOfmvzf6UOwXvM900g8VxQdoXrW3Pdy8q6Xov/lMf+lCtRab2rmxbZ6lTJePWAIJLb6EHlp/WuhaM0nklxXkc8Cuk4rDjSBetbeTCsuq/oT9z/I0wityZvflvKjGWCSNLR0KyD2jyrh/w8r08l7f0H6htS4MBavk3B1a2j2TPZyrHPNr7pNekwRcXxz7zNJ2uSzFKygNlsCGX1Imdxzp04uuUvgRGm65F+OPbOgHkBA+wUqUVF0hlVwWv9GX61/4UqoAaqTsJjU0BY0w9w9WLYQyM0nJJGaNu6Vmrq6ozSj6zlfl38iK3aN8BmjWchyyBpPdRXcGvV8Pp8T1rgyZShBbtDsnUxuO+NYOsTR2BRe676cdSvFi7dcjISVEnskHbmKGm30LY1DGrs1/ybcZxLXjYe43V27L5UP7JWAOU6VzNbigo7q5sVqYR27ku5nMb0hx162yXL7MjbqY1g+zvFbIaTGvWijRHBBO0i7onxlbDvh7/aw17s3ByXkHHcR3+Q7hS9Thb9aP3l0/Yrmxt+tHqh9icIvCLdx1YPiL2ZbLD9i34vbtWeMnqpJNequvtYlSedpdl195jcBxa/YYvZuMjOO0dydZ51tnihNJSRplCMlTRu+l3STE2XsBLrLnw9tzqACxmSfbWLS6fHNStd2YsWKMk/eYzF4xLrm7d7TN6zFpLGImByrfGCiqXQ0KM4qosljiQtk9W0JOiMCY79afjzzhwi63V6yD8JxjPu1u1rudTy5SO8/ZRl1+SP3YWMUUK7mDQtPXKxZhoB3kTz5SfsrLHJKcuY1YSdRbGF/iHUl7THPkJUZl3jaTP9K2/aJwe1q0Kxyc4qXmCXuLEwwYDKZVAuh9utUepyNrjgZQHxV0a4WRiwMEmI15iKpklulZGNya9ZUOOD4wNaZRAe3bZvUEEL5zM1ox5mo0u3sE5ZyhJccNpAR6Q3e5PsP+dV+1z9hopFeKAusCXQHsiFWNz7eU0qc3N2xXiNdgjC4k28qKUYay2WSOff7qZDM4KlQb21dFt/i9wLM228gv/wDW1Xeqn7AjK3VAa8QNxu3kWFaI0mY3112pGTK59S2RccDv5OP16/Wj+TiKWMFfSj119t3+dcoAp4lHUYdwFVmFzMVETDQJjyqX0MuG/EnFvhV+QRYwDoOrD2zdAz9Uc07TE+rMCYny8qsuCks0ZetT29L4/wBzkpdY2VGQ9dlhgDoQYIOvLnRbJuEVJu/Vv6+PYlrDlrbBnRUzFFcqxLERJETA2k/1mjsEppSVJt9a44OsNcv2mu22Zibak5MxgnTu1iDNMxuXPsGJY8iU0uoHhiLjyyLorEAAjORrB11qI+tLlf5GvhBeAh1UkBQXKlRIVhlJ1WYkHnTIVJJtd/0KyXJVcCFfUVT1QeQNZDRprtFQ0munayxfxA2+2rMDlXs6MWB5do6Qfsqcm3lP9SsV5AeDV7dvrSkozEBvNQJET3MPtrJHLDc4d+pOTHuCOG4xrd+1iLeQG24K5pGYzJ/MnalaqMcsJY30aJgto64tieE3bz3XTHK7tLJbNsrJ3yk67/vrn4Ya3HjUIyg0u7uxnAH0g4sMY1u3aQ2bOGQJat+s0EgEnvO0+ytmg0TxKUpSuUnbf7LyKTlQtyuTHWasWy9ka5dO/QVv2drFbYeRBbcyucEwoYEaDOQNCNyJFGx9PrkKiua+kXcNxIwtyzfRUuMjvpcHZaIGonbWaTqdNHNheO6vuuGNxye6zaD5V8QiBxhsMpMjRW/eGrhv+HcDXM5fiv2GrVS3uNI8b5UcWwk4XBsTGhUk9rae1zqy/hvElxOX4r9i/wBofkYDF5rl2TlAuOzAKRAJMkA8t418q7kMTjGML9ghvubzC/KhioGXC4MQco7JGv3t64f/AMdxy5eSX4r9h32hrsdv8q+LZczYbCGBMMGJiY2Ld9VX8N4UrU5fiv2J+0PyMdxrjb4vEPdZLNotbylV7K6RtJ35119Fplpsfhp316+0Tkludg+JzdXPV+tlDOGBBy7QBtNbpXt6eXIuNbuotxBlqTN8jWEv9GX61/4UqpBOGj1xBIZcunIkiNCROtXh3F5OwRi75yNlDqCbZBOmgXL399WlLjgXBLcr9v5lpHzA1HqankYbNl9bf3e+p/tI/v8Aj9MJZLzp16W26r5xswAkaFSR2ySASJgDlSJavEp7L58vf0LRwuj3+zMRKA2rn6vISIJkkx+1ykaGDS/t2D/u7F/CfPvsJ+T3EJZxsXWyC5bKgt/fylZ7pH76Tq054/V5p/kL1MW4cAfFuiOKw6vcfJkU+sHGsmBAmedXx6mE2kuvuLQzwk6QR0RwFpQ2NxJHV2dUSdbj8hG8Ax5e4Gq6icpPw4dX1fkiuaTfqR6sZYPjA4mlzDYllW7JuYdzACn/AIZPdFKli+ztTh06NfqUePwWpR6dzGYuwyEIw7QkEd0E929dC7SaNSafJuePcHfHphr+GKOFsrbdS4Uqy7zPt/KufhyrC5RyLvZkx5Ficoy8zPYHDGw+JRgpa3aPMMJlSNdjXSwzUouS8i2dqeyu7D7OILXLCkL89aJudkdowwHLSI5U5O2vajNKFRk7+6+PZ0Flm71GGtukC5dLyxUEwpAyidBMzPlSrcYpruaXHxcsoy6KuPeWYhQ6YfEEAO1zK0CA0HQx31Z8pSKRbjKePslaCMXxJhjGtZV6trmVlyjtSYJJ3nXvqXN767FIYV4CnfNXYlvXGsX7gtmMrMoO+k+dLb2ydGqKWXGtwf0pH+0cvUXfTlV8v3hWjdYviyngPrX9v1Fzb3VWHf3FtQ+I/wCpFPR/Crcvoj6rqSO+AT/SoxpOVMtqJuGNtdR5auq5Zb17DG0wICruvcV7IOntpqd/eaoyNOKThGV/n8zPWcPcdotydQIBjcHz8jSX1N05wjzIIOEeAMjSQIBffUCcs7Tp5VPHkU8XHd38jxcKyMSyQMjDcHUaHv1BqsgeSM16r8h58nH69frR/JxFQPFfSf8AWLO03f51ygCrHXrLWbdtS82w0E5YOYzrDaVdpGfHjyRySk65rz7fAv8A7Vt5/wBIyt1xWIzDJOXLmjfbWO/nR7Rf2aWzw7W359bryKMFxQW7bIQSwzdW3Jc4yt+WoqLrgvl0++alfHF+2uUXcO4rktdUXuKFYlWtsAddwQd9pnzqV7yuXS7p71T94Bdxs3C4LyWkMW7cabnY6VS2naY/HDbFL8ugxv3sMWDdbeYg6SYI0PMIY7Ue7lWfxdU+XV/59/kNqJ3wq7bdS965DbBiwle0nqr5jNLcqdkyZNyaM+TcnUUcizZykm5GuWM6zl5roSInUEfadar4k/kG6fkBDElkIzOE8OYfZrqRT/EdU2Wdpj3gfGEw9qzbZyF628bigyCrWwqyBvrOlcnU6WWScpJdo1707Y6E10O8Fx6yvUk3GyL+jDqcphGtspe4DsZysdNTnM1TJpcj3JR5e71r6pp0vmvZwWTQZa6QW2RC9wkjNDkmUm0FLCCGnONgZ1kUt6Oab2r4cc+tdeXT4dg3oz/E+JK91m7LyqLnSQTlGpPWSWJ5k6mK62jh4WOmvmuPw4r2C5pydi1sUZaIUGYAgxOh15ad1ad3UmMF3O7Tuw0YACOag6bb6mKjxEuAahZxjXJ7LmY1G3PfbTWhzUl1JSh2PbsdSsEaHUSJ3PKf6VXsJX9RltzFrlWDJXLlGvLfNyPPamuapUXo6wzoVDssBCdAeZI1gmTSXlSklX5lZKfY8UhpyFFVXDgO0GYHfvqKiWbbSrvZaMW1yeHEIbeUty219YmdeUU/dFxoKdnGDvBbmbMg03KkjlsAJnz9tVhKpWQ1aLOIYq2w0Z2aec5fsJJq05xf1wEE0LnaTNJbsuFv9GX61/4UqAKMLOYa5fP2a1MepWXQuN3T9b7BH+oq3xIUVfQ8DAbXDv3VN+0nnyD04yUtqilWypdUGDPzvrHfccqyT0sJScr6tP8AAspMPvdL75LNn1KsIliJMGQCTl2iKQvRuBKv0XYnexdexNu411mCAuxCgDRRELBJkAafZW7FCOOG27+uoie+00d3msksSymSNecQBpry19tMbiKW9JKioGyZPZ9ZSNI00Bny0JgVFxLeuVPaTrM2a3l7h7PD7dYqOLLKUnGqdnadWMuuocEtAGgnaDsRGntq1IHGfPu8zhraFbadYB22kxoAY138vzqmRuMLXJeKe5tryDMJYt21uDrrbdYmTfaZM/8ASPtFIjqJK1sYTx7mn5OwazxfK9lsn6pCkTvvrtpvWpT5T8hbwXGSvq7PcLjlW31bhbqTIUyCp8mG1SmkqfJM8Vy3RdM5xHEM7J6qJbPYQTG879576hyt+4mGHanzbfVhj8aQubpt2+sk5W107iRsSO/Sr71d9xS0zUdm50LbN23mZ7o6wnWJK6nWZANLW3q+R8oypKLr5hnGeJWr3a6uHgANmMADyjuq05Rl7xWHDLHxu49xMFj7NoEC1mJQozZyJB3gRptUqUYk5MM5v73e+gOL6LcFyz83liJJaT37DSNIqvF2uC/htxcZu/kE3eIWCCepthj+12o15hOX21ZyiUWGa/vdfXcDw+KNvMVYSwjY8oOnnpHvNUddbGZManVjJOIKQLjXV6zUxkMjtZsoM7Se7vrO8mTdSj8bFrTQqua/xVi7ieIzQoYMoLMIHiMkH7B9tXhKTXrIZDFGDtez5Gg+Tj6Qv1o/k4irDBX0p9dfbd/nXKAElAEoAlAEoAlADTo1wn9KxCWM4TMHOY7DKjPrOw7MTyoA04+Ti4bV64LmYWhYMoMytnRHuQ4MQiuCD+1rtQDKul3QVcFae6bxcDELbWFALW2Rj1nraHOjpHep1qEwOcT0JtuM2Gv9kWUuscQFt/rATbVSGYFjlaZgDTvoBAfEehrWLD3rl5NLdm4qqrSyXiQpkqMphSYP5VPcFyO8Z8mTKspfDEkgAiAJcdUSQT69jNd0BPZjWoASt0JuBQxv2QrB3U9vW2lpbpeMkgZHXsxmk7aTUgFehdtbuJR713LZurZU2rJuMzMCQSgYEL2eUk8hR2A4ToDecoLdy321tFQ0gkMllnOgIARr6jUydYFS+HRCZxh+g1zJ1ly6iKbTugAYlitp7uXaBompJG+k1C5+vrzJ70ZKgCUASgCUASgCUASgCUASgA1/oy/Wv/ClAAVAEoAlAEoAlAEoAlAEoAf9CuC28XiequdZlyM0WhLEjYaKxj2Kx8uYlEGmxXQTCqot9c4xVy6yW0LKZAvm3qipAAtqWLZ9CCIqES+Axfk1wxN0i8+QPba2wZGDWcua6cygqXUBogx2TQupD4M5h+CYMXsfaujEN+i9aUKOglUuBAGm2dTIMiNtqjtZPcOxXycFDdH6Rm6qybpy2m7UFgVWSAxMSpB1AY6ZdZboF2LMB0HwzYnFWXvXVTDPbBY5QSjhlBgg/wC+NoTzViaA/a/3Pbvybg3Mq3yALgtklMwBDLbcFwQM4uEkJuVEzQD4FuI6IW1wi4jrnId7IVimVAtxrglmzGWAQEqD2ZjWjvQeY1xHQC0Xe2gxNkr2Ve+Fy3PnrdvOgUAlSrkgczlhjrARYEPk7cxF3smJLWyuSeoyi4MxyN8/sdsh35RZIm6X8CXB3LSKbhz2Q7dYmQzndfU3UQo3JqQENAEoAlAEoAlAGv8Ak4/Xr9aP5OIoAV9KfXX23f51ygBJQBKAJQBKAJQBZYvMhzIzK2olTB1EHUd4JHvoAvHFL/Z+eu9gEJ227IICkLroCoCwOQAoA8xPEb1wRcu3HEgwzkiQWIME97sf+Zu80Ae2uKX1nLeurKZDDsJTwmD6vltQB1e4viHBVr91lbQg3GIOs6gnXUT7aAPP7VxGnz13QoR220KCEO+6jQdw2qbCj08XxGcXOvu5wSwbrGzAsAGIMyCQACeYAqAPbXGMSru637yvc0uMLjBn/wARBlvfQByvFsQFyi9dCypjO0SgAUxO6hVA7sojagC1+O4s5pxN85xlebrdoQRDa6iCRB7z30ALqAJQBKAJQBKAJQBKAJQBKADX+jL9a/8AClAAVAEoAlAEoAlAEoAlAEoA6RiDIJB7xQBBcPedNtaAPRdaIkx3TRYHmc66nXfzoA965vEdI5921AHhuHvPdv3f+KLA961vEd5359/t86APOsMRJjunT7KAPTdbvO0b8hsKLAhutr2jrqdd/b30AeXLhYySSfM0Ac0ASgCUASgCUAa/5OPpC/Wj+TiKAN9i+gmHLNL3T2mIkWjEsWIBNomJJ50AU+gGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GgCegGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GgCegGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GgCegGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GgCegGG8T/AHLPwagCegGG8T/cs/BqQJ6AYbxP9yz8GgCf+n+F8T/cs/BqAJ6AYbxP9yz8GpAnoBhvE/3LPwaAJ6AYbxP9yz8GgCegGG8T/cs/BoAnoBhvE/3LPwaAJ6AYbxP9yz8GgCegGG8T/cs/BoAnoBhvE/3LPwaAOj0Cw8AZ7kAkxls7mB/wfIUAc+gGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GgCegGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GgCegGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GgCegGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GgCegGG8T/AHLPwaAJ6AYbxP8Acs/BoAnoBhvE/wByz8GoAnoBhvE/3LPwakCf+n+G8T/cs/BqAJ6AYbxP9yz8GpAnoBhvE/3LPwaAJ6AYbxP9yz8GoAnoBhvE/wByz8GpAnoBhvE/3LPwaAJ6AYbxP9yz8GgCegGG8T/cs/BoAY8A6FWLd9GV7mhJiLYBOR11y2gdAx586AP/2Q==.jpg")



## Future Enhancements
- Improve classification with **# Deep Learning (LSTMs, Transformers)**.
- Implement **# real-time SMS filtering**.
- Deploy on **# Heroku/AWS**.

## Contributing
Fork the repository and submit pull requests to contribute.

## License
This project is licensed under the **# MIT License**.

---
### Stay Safe from Spam! 📩🚀

