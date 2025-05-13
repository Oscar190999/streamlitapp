{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "76ca779f-7421-4e5c-a13a-ab5ce9b4850c",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1839885029.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[1], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    ```python\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "```python\n",
    "\n",
    "\n",
    "import streamlit as st\n",
    "import requests\n",
    "\n",
    "st.title(\"Crypto Price Notifier\")\n",
    "\n",
    "\n",
    "API_KEY = \"c079302c-cdd5-47be-934d-2bd4ca0b91bf\"\n",
    "HEADERS = {\"X-CMC_PRO_API_KEY\": API_KEY}\n",
    "\n",
    "# Inputs\n",
    "crypto = st.text_input(\"Cryptocurrency symbol (e.g. BTC):\", value=\"BTC\").upper().strip()\n",
    "fiat   = st.text_input(\"Fiat currency (e.g. EUR):\", value=\"EUR\").upper().strip()\n",
    "threshold = st.number_input(f\"Threshold value ({fiat}):\", min_value=0.0, value=300.0)\n",
    "\n",
    "if st.button(\"Notify me\"):\n",
    "    \n",
    "    url = (\n",
    "        \"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest\"\n",
    "        f\"?symbol={crypto}&convert={fiat}\"\n",
    "    )\n",
    "    resp = requests.get(url, headers=HEADERS).json()\n",
    "    data = resp.get(\"data\", {})\n",
    "    \n",
    "    if crypto not in data:\n",
    "        st.error(\"Cryptocurrency not found. Please check the symbol and try again.\")\n",
    "    else:\n",
    "        price = data[crypto][\"quote\"][fiat][\"price\"]\n",
    "        st.write(\n",
    "            f\"The current price of {crypto} is {price:,.2f} {fiat}. \"\n",
    "            f\"We will notify you when the price reaches {threshold:,.2f} {fiat}.\"\n",
    "        )\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "82dc11a6-91c1-45c5-8223-8869eae82f78",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-06 10:12:49.518 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import requests\n",
    "\n",
    "st.title(\"Crypto Price Notifier\")\n",
    "\n",
    "# ← Replace with your real key, then remove before submitting\n",
    "API_KEY = \"c079302c-cdd5-47be-934d-2bd4ca0b91bf\"\n",
    "HEADERS = {\"X-CMC_PRO_API_KEY\": API_KEY}\n",
    "\n",
    "# Inputs\n",
    "crypto = st.text_input(\"Cryptocurrency symbol (e.g. BTC):\", value=\"BTC\").upper().strip()\n",
    "fiat   = st.text_input(\"Fiat currency (e.g. EUR):\", value=\"EUR\").upper().strip()\n",
    "threshold = st.number_input(f\"Threshold value ({fiat}):\", min_value=0.0, value=300.0)\n",
    "\n",
    "if st.button(\"Notify me\"):\n",
    "    # Fetch current price\n",
    "    url = (\n",
    "        \"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest\"\n",
    "        f\"?symbol={crypto}&convert={fiat}\"\n",
    "    )\n",
    "    resp = requests.get(url, headers=HEADERS).json()\n",
    "    data = resp.get(\"data\", {})\n",
    "\n",
    "    if crypto not in data:\n",
    "        st.error(\"Cryptocurrency not found. Please check the symbol and try again.\")\n",
    "    else:\n",
    "        price = data[crypto][\"quote\"][fiat][\"price\"]\n",
    "        st.write(\n",
    "            f\"The current price of {crypto} is {price:,.2f} {fiat}. \"\n",
    "            f\"We will notify you when the price reaches {threshold:,.2f} {fiat}.\"\n",
    "        )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f07f9383-2e75-4be7-90d7-e903ea26021f",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (420725208.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[5], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    streamlit run crypto_notifier.py\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run crypto_notifier.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23f112a2-1938-4705-9a84-c4a842614073",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
