export CUDA_VISIBLE_DEVICES=1
data_dir="path/to/data"
ckpt_dir="path/to/ckpt"
SCRIPTS="path/to/mosesdecoder/scripts"

MULTI_BLEU=${SCRIPTS}/generic/multi-bleu.perl
MTEVAL_V14=${SCRIPTS}/generic/mteval-v14.pl
DETOKENIZER=${SCRIPTS}/tokenizer/detokenizer.perl

src="mo"
tgt="en"

mkdir -vp ${ckpt_dir}/result/

fairseq-generate ${data_dir}data-bin \
    --path ${ckpt_dir}/checkpoint_best.pt \
    --arch transformer_iwslt_de_en --share-decoder-input-output-embed \
    --source-lang ${src} --target-lang ${tgt}  \
    --batch-size 128 --beam 8 > ${ckpt_dir}/result/bestbeam8.txt


grep ^H ${ckpt_dir}/result/bestbeam8.txt | cut -f3- > ${ckpt_dir}/result/predict.tok.true.bpe.en
grep ^T ${ckpt_dir}/result/bestbeam8.txt | cut -f2- > ${ckpt_dir}/result/answer.tok.true.bpe.en


sed -r 's/(@@ )| (@@ ?$)//g' < ${ckpt_dir}/result/predict.tok.true.bpe.en  > ${ckpt_dir}/result/predict.tok.true.en
sed -r 's/(@@ )| (@@ ?$)//g' < ${ckpt_dir}/result/answer.tok.true.bpe.en  > ${ckpt_dir}/result/answer.tok.true.en


${MULTI_BLEU} -lc ${ckpt_dir}/result/answer.tok.true.en < ${ckpt_dir}/result/predict.tok.true.en > ${ckpt_dir}/result/bleu_result.txt

${DETOKENIZER} -l en < ${ckpt_dir}/result/predict.tok.true.en > ${ckpt_dir}/result/predict.en