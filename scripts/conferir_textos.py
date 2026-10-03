#!/usr/bin/env python3
"""Confere data/i18n/textos.<idioma>.json contra o português: mesmas chaves, mesmos marcadores {assim},
mesmos trechos de código e nenhum valor vazio. Sai com código 1 se houver problema.

Uso: python3 scripts/conferir_textos.py es [fr ...]   (sem argumentos: todos os idiomas)
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import CODIGOS, J, textos_pt

MARCADOR = re.compile(r'\{[a-z_]+\}')
CODIGO = re.compile(r'`[^`]+`')


def problemas(lang: str, pt: dict) -> list:
    arq = J('data', 'i18n', f'textos.{lang}.json')
    if not os.path.exists(arq):
        return [f'{lang}: arquivo faltando']
    tr = json.load(open(arq, encoding='utf-8'))
    erros = [f'{lang}: chave faltando {k}' for k in pt if k not in tr] + [f'{lang}: chave sobrando {k}' for k in tr if k not in pt]
    for k, v in tr.items():
        if k not in pt:
            continue
        if not isinstance(v, str) or not v.strip():
            erros.append(f'{lang}: valor vazio em {k}')
        elif sorted(MARCADOR.findall(v)) != sorted(MARCADOR.findall(pt[k])):
            erros.append(f'{lang}: marcadores diferentes em {k}')
        elif sorted(CODIGO.findall(v)) != sorted(CODIGO.findall(pt[k])):
            erros.append(f'{lang}: trecho de código alterado em {k}')
        elif v.count('**') != pt[k].count('**') or v.count('](') != pt[k].count(']('):
            erros.append(f'{lang}: negrito ou link diferente em {k}')
    return erros


def main() -> None:
    pt = textos_pt()
    erros = [e for lang in (sys.argv[1:] or [c for c in CODIGOS if c != 'pt']) for e in problemas(lang, pt)]
    if erros:
        print(f'{len(erros)} problema(s):'); [print(' -', e) for e in erros[:60]]
        sys.exit(1)
    print(f'OK: {len(pt)} textos conferidos')


if __name__ == '__main__':
    main()
