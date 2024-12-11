# dork1

```
pipx install git+https://github.com/LocaMartin/dork1.git
```
```
my-cli-tool Alice
```

### usage:
domain file , inurl file & thread:
```bash
dork -d domains.txt -in inurl.txt -t 100
```
pass domains through other command:
```bash
cat domains.txt | dork -in inurl.txt -o output.txt
```
single domain:
```bash
dork -d www.domain.com -in inurl.txt
```
single inurl:
```bash
dork -d domains.txt -in "q="
```

### flags:

```bash
-d: single domain or domain file ( example.com )
-in: sigle inurl or inurl file ( q= )
-t: threads ( default 50 )
-o: output file ( output.txt )
-h: shows this message on the terminal
-version: check version of the tool
```
### contact:   