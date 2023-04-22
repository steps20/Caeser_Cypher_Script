# 🔒Caeser_Cypher_Script🔒
<div align="center">
<h1>Description: </h1>
Simple python script that has the abilities to encrypt or decrypt caeser cypher encrypted messages. You can also specifiy a file to encrypt or decrypt the whole file.
</div>

### USAGE: 
```bash
  python3 caec.py -e -t "Hello World" -s 6
```
output: nkrru cuxrj

```bash
  python3 caec.py -d -t "nkrru cuxrj" -s 6 
```
output: hello world

<h1>OR</h1>

```bash
  python3 caec.py [-e/-d] -f /Desktop/encryptedmessage.txt -s 6
```
