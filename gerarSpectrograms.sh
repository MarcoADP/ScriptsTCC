echo "GERAR ESPECTROGRAMAS"

#database_atual="elsdsr";
#pasta="train"
db=$1

#mkdir -p spectrograms
#mkdir -p spectrograms/${database_atual}/
#mkdir -p spectrograms/${database_atual}/
#mkdir -p spectrograms/${database_atual}/train/
#mkdir -p spectrograms/${database_atual}/test/
#mkdir -p spectrograms/${database_atual}/${db}db/train
#mkdir -p spectrograms/${database_atual}/${db}db/test


echo "criando espectrogramas de $pasta da base de dados"
cd audios_wav
echo($(ls | grep -i -E ".*\wav$"))
for musicFile in $(ls | grep -i -E ".*\wav$")
do
  musicName=$(basename $musicFile .wav);
  sox $musicName.wav -n remix 1 rate -v 6800 spectrogram -m -X 27 -r -z $db -o ../spectrograms_${db}/$musicName.png
done
