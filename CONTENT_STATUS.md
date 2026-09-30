# Conteúdo pendente para produção

Status em 29/09/2026. O protótipo principal já não depende de textos `todo` visíveis. As pendências mais claras agora são **ativos originais e aprovação editorial**, não layout.

## Imagens que ainda precisam de original/aprovação

| Uso | Estado atual | O que pedir à Nora |
|---|---|---|
| Home — bloco About | placeholder | 1 retrato profissional/autoral da Nora em alta resolução |
| About — retrato principal | placeholder | pode ser o mesmo retrato da Home ou uma segunda opção |
| Current — The Lost Paintings | placeholder | instalação/exhibition view autorizado |
| Current — Untitled: Palestine | placeholder | imagem representativa do pop-up/ongoing work |
| Current — Förkolnade Minnen / Muistoihin Hiiltyneet | placeholder | vista da exposição ou obra autorizada |

## Fotografias já utilizáveis como amostra

O protótipo usa o CDN público do Squarespace para demonstrar a estrutura:

- Portraits
- From Arrival to Belonging?
- Parfyymin tuulahdus
- Notes of Resistance
- Home / Current / manifesto visual

Essas referências são **amostras de migração**. Antes de produção, o ideal é substituir as imagens escolhidas pelos originais fornecidos/aprovados por Nora.

## Notes of Resistance

- 86 imagens do site atual estão catalogadas no inventário.
- 25 estão estruturadas no protótipo público atual.
- a página interna `/review/notes-of-resistance/` existe para fazer a seleção junto com Nora.
- a decisão final deve ser editorial: quais fotos ficam na sequência principal e se haverá um arquivo completo separado.

## Texto que merece confirmação de Nora

Mesmo quando baseado no site/CV atual, estes itens devem ser confirmados antes da publicação definitiva:

- posicionamento curto da Home;
- bio curta e bio expandida;
- ordem e seleção de projetos destacados;
- wording de Commissions;
- títulos provisórios/ongoing work;
- legendas, datas e locais de cada fotografia;
- datas/status de exposições futuras ou recém-encerradas;
- prazo de resposta no contato, se quisermos exibi-lo;
- versão em finlandês.

## Entrega de originais

Para cada imagem final, registrar:

```text
arquivo original
projeto
largura / altura
alt text
legenda
data
local
crédito
direitos / autorização
pode ser hero? sim/não
```

Evitar masters vindos de Instagram. O pacote de referência fornecido continua documentado em `REFERENCE_BUNDLE.md`.

## Versão em finlandês (/fi/)

- Todas as páginas principais têm versão finlandesa em `/fi/`, gerada por `build.py` a partir de `content/fi.json` (texto em inglês → finlandês).
- **A tradução é um rascunho e precisa de revisão por falante nativo** (de preferência a Nora) antes de publicar. Para corrigir, edite só o valor em finlandês em `content/fi.json` e rode `python3 build.py`.
- Nomes de projetos, títulos de obras e instituições ficam no original.
- `content/fi-missing.txt` lista qualquer texto novo do site que ainda não tem tradução (hoje: nenhum). Texto sem tradução aparece em inglês na versão FI.

