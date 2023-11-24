export CUDA_VISIBLE_DEVICES=1
data_dir="path/to/data"
ckpt_dir="path/to/ckpt"
src='mo'
tgt='en'

mkdir -vp ${ckpt_dir}

nohup fairseq-train \
    ${data_dir}/data-bin \
    --arch transformer_iwslt_de_en --share-decoder-input-output-embed \
    --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 \
    --lr '1e-05' --lr-scheduler inverse_sqrt --warmup-updates 4000 \
    --dropout 0.3 --weight-decay 0.001 \
    --max-epoch 3000\
    --seed 222 \
    --source-lang ${src} --target-lang ${tgt}  \
    --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
    --max-tokens 18000 \
    --eval-bleu \
    --eval-bleu-args '{"beam": 5, "max_len_a": 1.2, "max_len_b": 10}' \
    --eval-bleu-detok moses \
    --eval-bleu-remove-bpe \
    --eval-bleu-print-samples \
    --best-checkpoint-metric bleu --maximize-best-checkpoint-metric \
    --keep-last-epochs 10 \
    --num-workers 20 \
	--save-dir ${ckpt_dir}/ \
    --fp16 