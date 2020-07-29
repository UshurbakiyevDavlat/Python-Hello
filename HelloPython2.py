text = "X-DSPAM-Confidence:    0.8475"
ind=text.find('0')
res=float(text[ind:ind+6])
print(res)
