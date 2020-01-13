FROM lordobsidian01/dev:latest

COPY . /root/workspace

WORKDIR /root/workspace

RUN rm -rf build \
  && mkdir build \
  && cd build \
  && cmake ../{{ cookiecutter.project_name}} -DCMAKE_BUILD_TYPE=Release -DUNIT_TESTS=Off \
  && cmake --build . 

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]