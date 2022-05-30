# Strings

text = "X-DSPAM-Confidence:    0.8475"

a=text.find('0.8475')
c=a
print(text[a:a+6])
c=float(a)