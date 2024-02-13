FROM ubuntu:latest
LABEL authors="FlakeVic"

ENTRYPOINT ["top", "-b"]

CMD ["-d", "5"]

