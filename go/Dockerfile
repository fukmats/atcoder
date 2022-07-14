FROM golang:1.15.6

RUN apt update \
  && apt install -y vim \
  python3 \
  python3-pip \
  nodejs \
  npm \
  && pip3 install -U pip \
  && pip3 install online-judge-tools \
  && npm install -g atcoder-cli \
  && acc config default-test-dirname-format test \
  && acc config default-task-choice all \
  # コマンドアライアス
  && echo 'alias ojgo="oj t -c \"go run ./main.go\" -d test/"' >> ~/.bashrc \
  && echo 'alias addgo="cp /go/src/work/template.go ./main.go"' >> ~/.bashrc