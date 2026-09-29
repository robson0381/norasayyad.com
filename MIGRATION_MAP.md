# Mapa de migração — norasayyad.com

Levantamento do site público atual feito em 29/09/2026. Este arquivo separa **conteúdo a preservar**, **estrutura a melhorar** e **itens a remover**. O objetivo é reconstruir o site sem perder o que já funciona.

## 1. Rotas atuais → novas rotas

| Página atual | Nova rota | Ação | Observação |
|---|---|---|---|
| `/` | `/` | Melhorar | Preserva o papel de Home, mas troca a abertura genérica por posicionamento, projetos, credenciais, Current e Commissions |
| `/work-1` | `/work/` | Migrar + 301 | Mantém os quatro projetos atuais com navegação mais clara |
| `/work-1/project-one-f5w4d-z9nem-s3jda-eyssk-73f62-tmxz9-kllpy` | `/work/portraits/` | Migrar + 301 | 19 fotografias no site atual |
| `/work-1/project-two-ky966-n329z-nnx53-feazs-s32gp-b59d5-9c4hw` | `/work/from-arrival-to-belonging/` | Migrar + 301 | 10 fotografias + texto original do projeto |
| `/work-1/parfyymin-tuulahdus` | `/work/parfyymin-tuulahdus/` | Migrar + 301 | 3 fotografias; precisa statement/contexto |
| `/work-1/notes-of-resistance` | `/work/notes-of-resistance/` | Migrar + 301 | 86 fotografias no site atual; preservar arquivo completo, mas não carregar tudo de uma vez |
| `/about` | `/about/` | Preservar + reorganizar | Bio e CV são fortes; passam a ter hierarquia editorial e download de CV |
| — | `/news/` | Novo | Current, exposições, imprensa e agenda |
| — | `/services/` | Novo | Commissions / editorial / talks / workshops |
| — | `/contact/` | Novo | Contato e formulário por assunto |

## 2. O que o site atual faz bem e deve permanecer

- Fotografias e quatro projetos já publicados.
- Texto de **From Arrival to Belonging? A Decade in Portraits**.
- Bio extensa e currículo profissional do About.
- Credenciais reais: imprensa, exposições, acervos públicos, residências, ensino e clientes.
- Navegação simples e pouca distração visual.
- Uso do próprio trabalho fotográfico como elemento principal, sem excesso de UI.

## 3. O que será melhorado

- Home deixa de ser apenas “A visual storyteller” e passa a explicar rapidamente quem é Nora e o que ela faz.
- Identidade principal passa a ser **Editorial / Archive in Motion**.
- Work deixa de depender de hover e passa a funcionar igualmente em mouse e toque.
- Projetos ganham statement, ficha técnica, narrativa, capítulos quando necessário e navegação anterior/próximo.
- About deixa de ser um bloco corrido e vira bio + CV organizado.
- Current traz exposições e publicações recentes para a superfície.
- Commissions cria um caminho explícito para trabalho editorial/institucional.
- URLs ficam legíveis.
- Alt text, SEO, Open Graph, foco de teclado e estrutura semântica entram como requisitos.
- Imagens usam `srcset`, lazy loading e curadoria para evitar páginas excessivamente pesadas.

## 4. O que será removido ou não reproduzido

- `Login / Account` e carrinho quando não houver uso real de commerce.
- URLs geradas como `project-one-f5w4d...`.
- Dependência de hover para descobrir conteúdo.
- Meta description vazia.
- Imagens sem descrição alternativa ou com nome do arquivo usado como descrição.
- Galeria de 86 imagens carregada integralmente logo na entrada.

## 5. Inventário visual

O site público atual contém, por página:

| Área | Quantidade observada |
|---|---:|
| Home | 1 imagem principal |
| Portraits | 19 |
| From Arrival to Belonging? | 10 |
| Parfyymin tuulahdus | 3 |
| Notes of Resistance | 86 |
| **Total de posições observadas** | **119** |

Há imagens repetidas entre áreas, portanto “119” não significa 119 arquivos únicos.

O protótipo já possui 58 referências estruturadas em `content/photos.json` com URL, dimensões e alt text: 1 hero, 25 de Notes of Resistance, 19 Portraits, 10 From Arrival to Belonging? e 3 Parfyymin tuulahdus.

O arquivo `content/current-site-inventory.json` preserva o inventário completo de **Notes of Resistance (86 URLs do CDN atual)**. Essas imagens são tratadas como **amostras temporárias**. A versão final deve trocar as referências do CDN/exports por originais fornecidos pela Nora.

### Estratégia de amostra x produção

- **Amostra:** usar o CDN atual para reproduzir visualmente o conteúdo sem duplicar arquivos recomprimidos.
- **Produção:** Nora fornece os originais; cada arquivo recebe ID estável, dimensões, alt text, legenda, projeto, data/local e status de autorização.
- **Archive:** manter as 86 imagens catalogadas.
- **Narrativa publicada:** mostrar uma seleção curada por padrão para preservar ritmo e performance; o arquivo completo pode ser acessível separadamente se Nora quiser.

## 6. Redirecionamentos obrigatórios na migração

Os caminhos antigos devem responder com **301 permanente** para as novas URLs. A especificação independente de plataforma fica em `content/redirects.json`.

Isso permite trocar Squarespace por outra hospedagem sem perder links já compartilhados e reduz o impacto de SEO da mudança.

## 7. Pendências que dependem da Nora

1. Escolher o retrato profissional para Home/About.
2. Enviar originais das fotografias selecionadas para produção.
3. Confirmar seleção final de Notes of Resistance.
4. Confirmar statements e legendas dos projetos.
5. Confirmar datas/local de exposições e o conteúdo de Current.
6. Definir se haverá venda de prints.
7. Aprovar EN e, depois, fornecer/revisar FI.
8. Confirmar o e-mail público definitivo e eventual endereço `@norasayyad.com`.

## 8. Critério de conclusão da migração

A troca do site atual só deve acontecer quando:

- conteúdo crítico estiver aprovado;
- redirects estiverem testados;
- páginas desktop/mobile estiverem revisadas;
- formulário funcionar;
- originals/substituições estiverem concluídos ou claramente aceitos como provisórios;
- analytics e Search Console estiverem preparados;
- DNS e e-mail tiverem plano de rollback.
