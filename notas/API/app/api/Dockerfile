FROM continuumio/miniconda3
EXPOSE 8080
COPY ./environment.yml /app/environment.yml
RUN conda env update -f /app/environment.yml
COPY . /app
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "est_comp", "python", "/app/app.py"]
