# https://google.github.io/styleguide/jsoncstyleguide.xml?showone=Property_Name_Format#Property_Name_Format


keys = ['Empresa', 'Razão Social', 'Situação Registro', 'Situação Emissor', 'Segmento de Listagem', 'Atividade', 'Ação', 'Data Cotação', 'Tipo de Ação', 'Último Fechamento', 'Fator de Cotação', 'Volume Financeiro', 'Último Demonstrativo', 'Setor', 'Subsetor', 'Segmento', 'Part. Índices', 'Preço/Lucro', 'Preço/VPA', 'Preço/Receita Líquida', 'Preço/FCO', 'Preço/FCF', 'Preço/Ativo Total', 'Preço/EBIT', 'Preço/Capital Giro', 'Preço/NCAV', 'EV/EBIT', 'EV/EBITDA', 'EV/Receita Líquida', 'EV/FCO', 'EV/FCF', 'EV/Ativo Total', 'Receita Líquida', 'Resultado Bruto', 'EBIT', 'Depre/Amort', 'EBITDA', 'Lucro Líquido', 'Menor Preço 52 sem.', 'Maior Preço 52 sem.', 'Variação 2020', 'Variação 1 ano', 'Variação 2 anos (total)', 'Variação 2 anos (anual)', 'Variação 3 anos (total)', 'Variação 3 anos (anual)', 'Variação 4 anos (total)', 'Variação 4 anos (anual)', 'Variação 5 anos (total)', 'Variação 5 anos (anual)', 'Volume Diário Médio (3 meses)', 'Retorno s/ Capital Tangível', 'Retorno s/ Capital Investido', 'Retorno s/ Patrimônio Líquido', 'Retorno s/ Ativo', 'Margem Bruta', 'Margem Líquida', 'Margem EBIT', 'Dividend Yield', 'Giro do Ativo', 'Alavancagem Financeira', 'Passivo/Patrimônio Líquido', 'Market Cap', 'Enterprise Value', 'Lucro/Ação', 'Valor Patrimonial da Ação', 'Disponibilidades', 'Ativo Total', 'Dívida CP', 'Dívida LP', 'Dívida Bruta', 'Dívida Líquida', 'Patrimônio Líquido', 'Quant. Ações Ordinárias', 'Quant. Ações Preferenciais', 'Quant. Ações Totais']
translationTable = str.maketrans("éàèùâêîôûçõóíãáúü"+"éàèùâêîôûçõóíãáúü".upper(), "eaeuaeioucooiaauu"+"eaeuaeioucooiaauu".upper())

def to_camel_case(key):
    key = key.translate(translationTable)
    words = key.split(' ')
    return words[0].lower() + ''.join(x.title() for x in words[1:])


def clean_string(keys):
        
    new_key = []
    for key in keys:
        key = key.replace(".","").replace("s/","Sobre").replace("(","").replace(")","").replace("/"," ")
        new_key.append(to_camel_case(key.translate(translationTable)))
    return new_key


new_keys = clean_string(keys)
display_keys = dict(zip(new_keys, keys))