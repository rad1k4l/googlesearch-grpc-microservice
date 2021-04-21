# Googlesearch API gRPC Microservice

Googlesearch API is gRPC microservice version of [MarioVilas/googlesearch](https://github.com/MarioVilas/googlesearch) library.

## Installation

Clone repository.

```bash
git clone https://github.com/rad1k4l/googlesearch-grpc-microservice.git
```

Install requirements

```bash
pip3 install -r requirements.txt
```
Generate proto files

On linux machine: 

```bash
bash proto_gen.sh
```

On Windows OS: 

```bash
.\proto_gen.bat
```

## Usage

Simply run search.py: 
```sh
python3 search.py
```
If you need change gRPC listen address pass it as `--address` argument:
```sh
python3 search.py --address="localhost:43420"
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
