

import streamlit as st
import pandas as pd
dados_ubs = {
    "micro_08_equipe_316": {
        "profissionais": ["Acs-Adriano", "médica - Mirian", "sem enfermeira."],
        "enderecos": [
            {"rua": "rua hipolito pamplona", "inicio": 640,
                "fim": 783, "lado": "todos"},
            {"rua": "rua joquim rodrigues", "inicio": 67,
                "fim": 169, "lado": "impar"},
            {"rua": "rua 3 tupinamba da frota",
                "inicio": 993, "fim": 999, "lado": "impar"},
            {"rua": "rua 5 tupinamba da frota",
                "inicio": 815, "fim": 960, "lado": "todos"},
            {"rua": "rua 1 tupinamba da frota",
                "inicio": 974, "fim": 1107, "lado": "todos"},
            {"rua": "rua 2 tupinamba da frota",
                "inicio": 979, "fim": 1073, "lado": "impar"},
            {"rua": "rua salvador", "inicio": 700, "fim": 1001, "lado": "impar"}

        ]
    },
    "micro_07_equipe_316": {
        "profissionais": ["Acs-Valéria", "médica - Mirian", "sem enfermeira."],
        "enderecos": [
            {"rua": "rua hipolito pamplona", "inicio": 638,
                "fim": 324, "lado": "par"},
            {"rua": "rua joquim rodrigues", "inicio": 64,
                "fim": 140, "lado": "impar"},
            {"rua": "rua 3 tupinamba da frota",
                "inicio": 976, "fim": 1106, "lado": "par"},
            {"rua": "rua 5 tupinamba da frota",
                "inicio": 961, "fim": 974, "lado": "todos"},
            {"rua": "rua 4 tupinamba da frota",
                "inicio": 943, "fim": 1066, "lado": "todos"},
            {"rua": "rua 2 tupinamba da frota",
                "inicio": 974, "fim": 1072, "lado": "par"},
            {"rua": "rua salvador", "inicio": 30, "fim": 1068, "lado": "impar"},
            {"rua": "rua tenente queiros", "inicio": 1213,
                "fim": 1213, "lado": "todos"}
        ]
    },
    "micro_03_equipe_316": {
        "profissionais": ["Acs-Gabriela", "médica - Mirian", "sem enfermeira."],
        "enderecos": [
            {"rua": "rua major celestino", "inicio": 870, "fim": 1080, "lado": "par"},
            {"rua": "rua major celestino", "inicio": 1105,
                "fim": 1161, "lado": "todos"},
            {"rua": "rua pedro melo", "inicio": 1241, "fim": 1295, "lado": "impar"},
            {"rua": "rua tenente queiros", "inicio": 957,
                "fim": 1185, "lado": "impar"},
            {"rua": "rua tenente queiros ", "inicio": 1138,
                "fim": 1162, "lado": "par"},
            {"rua": "rua doutor manoel soares",
                "inicio": 890, "fim": 1120, "lado": "todos"},
            {"rua": "rua 7 tupinamba da frota",
                "inicio": 5, "fim": 41, "lado": "todos"},
            {"rua": "rua 3 tupinamba da frota",
                "inicio": 981, "fim": 985, "lado": "impar"},
            {"rua": "rua hipolito pamplona", "inicio": 344,
                "fim": 400, "lado": "todos"},
            {"rua": "rua hipolito pamplona", "inicio": 639,
                "fim": 639, "lado": "todos"},
            {"rua": "rua salgado filho", "inicio": 770, "fim": 1094, "lado": "par"}
        ]
    },
    "micro_01_equipe_316": {
        "profissionais": ["Acs-Roberto", "médica - Mirian", "sem enfermeira."],
        "enderecos": [
            {"rua": "rua tomas rodrigues", "inicio": 1330,
                "fim": 1388, "lado": "par"},
            {"rua": "rua padre perdigao sampaio",
                "inicio": 850, "fim": 1122, "lado": "par"},
            {"rua": "rua salgado filho", "inicio": 773, "fim": 914, "lado": "todos"},
            {"rua": "rua salgado filho", "inicio": 935,
                "fim": 1073, "lado": "impar"},
            {"rua": "rua major celestino ", "inicio": 997,
                "fim": 1073, "lado": "impar"},
            {"rua": "rua padre jose arteiro",
                "inicio": 666, "fim": 680, "lado": "impar"},
            {"rua": "rua padre jose arteiro",
                "inicio": 669, "fim": 769, "lado": "todos"},
            {"rua": "rua tenente queiros", "inicio": 827,
                "fim": 900, "lado": "todos"},
            {"rua": "rua hipolito pamplona", "inicio": 985,
                "fim": 1009, "lado": "todos"},
            {"rua": "rua pedro melo", "inicio": 1139, "fim": 1181, "lado": "todos"}
        ]
    },
    "micro_03_equipe_315": {
        "profissionais": ["Acs-Viviane", "médico - Adryan", "enfª Ana Paula girão."],
        "enderecos": [
            {"rua": "rua salgado filho", "inicio": 272, "fim": 754, "lado": "par"},
            {"rua": "rua major celestino", "inicio": 579,
                "fim": 848, "lado": "todos"},
            {"rua": "rua hipolito pamplona", "inicio": 283,
                "fim": 343, "lado": "todos"},
            {"rua": "rua travessa brito barbosa",
                "inicio": 10, "fim": 32, "lado": "todos"},
            {"rua": "rua pedro melo", "inicio": 1244, "fim": 1270, "lado": "par"},
            {"rua": "rua professor jose leite gondim",
                "inicio": 1300, "fim": 1330, "lado": "todos"},
            {"rua": "rua coronel joaquim franklin",
                "inicio": 911, "fim": 1115, "lado": "todos"},
            {"rua": "avenida mister hull", "inicio": 5759,
                "fim": 5881, "lado": "impar"}

        ]
    },
    "micro_01_equipe_315": {
        "profissionais": ["Acs-Nazaré", "médico - Adryan", "enfª Ana Paula girão."],
        "enderecos": [
            {"rua": "rua salgado filho", "inicio": 8, "fim": 100, "lado": "par"},
            {"rua": "rua sao vicente de paula",
                "inicio": 129, "fim": 429, "lado": "impar"},
            {"rua": "rua hipolito pamplona", "inicio": 2, "fim": 104, "lado": "par"},
            {"rua": "rua cantor carlos augusto",
                "inicio": 13, "fim": 234, "lado": "todos"},
            {"rua": "travessa sao vicente de paula",
                "inicio": 51, "fim": 133, "lado": "todos"},
            {"rua": "avenida mister hull", "inicio": 5826, "fim": 5900, "lado": "par"}

        ]
    },
    "micro_06_equipe_315": {
        "profissionais": ["Acs-Mopse", "médico - Adryan", "enfª Ana Paula girão."],
        "enderecos": [
            {"rua": "avenida mister hull", "inicio": 5988,
                "fim": 6018, "lado": "par"},
            {"rua": "rua cantor carlos augusto",
                "inicio": 97, "fim": 219, "lado": "impar"},
            {"rua": "rua padre perdigao sampaio",
                "inicio": 475, "fim": 692, "lado": "todos"},
            {"rua": "rua martins neto", "inicio": 1055,
                "fim": 1087, "lado": "todos"},
            {"rua": "rua jose leite gondim",
                "inicio": 1102, "fim": 1226, "lado": "par"},
            {"rua": "rua coronel joaquim franklin",
                "inicio": 808, "fim": 860, "lado": "par"},
            {"rua": "rua toms rodrigues", "inicio": 428, "fim": 460, "lado": "par"},
            {"rua": "rua salgado filho", "inicio": 235, "fim": 701, "lado": "impar"}

        ]
    },
    "micro_04_equipe_315": {
        "profissionais": ["Acs-Irapuan", "médico - Adryan", "enfª Ana Paula girão."],
        "enderecos": [
            {"rua": "rua anario braga", "inicio": 810, "fim": 1009, "lado": "todos"},
            {"rua": "rua tomas rodrigues", "inicio": 6, "fim": 135, "lado": "todos"},
            {"rua": "rua padre perdigao sampaio",
                "inicio": 129, "fim": 354, "lado": "todos"},
            {"rua": "rua jose acioly", "inicio": 437, "fim": 505, "lado": "todos"},
            {"rua": "rua presidente prudente",
                "inicio": 14, "fim": 80, "lado": "todos"},
            {"rua": "rua sao vicente de paula",
                "inicio": 45, "fim": 55, "lado": "todos"},
            {"rua": "travessa vicente sales",
                "inicio": 16, "fim": 80, "lado": "par"},
            {"rua": "rua professora raimunda adelia",
                "inicio": 6, "fim": 232, "lado": "par"},
            {"rua": "travessa anario braga",
                "inicio": 30, "fim": 65, "lado": "todos"},
            {"rua": "rua salgado filho", "inicio": 15, "fim": 81, "lado": "todos"}

        ]
    },
    "micro_99_equipe_320": {
        "profissionais": ["Área Sem agente de saúde", "médico - Ewaldo", "enfª Adriana catunda."],
        "enderecos": [
            {"rua": "rua joaquim leitao", "inicio": 587,
                "fim": 707, "lado": "impar"},
            {"rua": "rua tenente queiros", "inicio": 584, "fim": 698, "lado": "par"},
            {"rua": "rua hugo vitor", "inicio": 375, "fim": 598, "lado": "todos"},
            {"rua": "rua coronel joaquim franklim",
                "inicio": 473, "fim": 633, "lado": "impar"},
            {"rua": "rua coronel joaquim franklim",
                "inicio": 658, "fim": 736, "lado": "par"},
            {"rua": "rua pedro melo", "inicio": 703, "fim": 786, "lado": "todos"},
            {"rua": "rua jose leite gondim",
                "inicio": 21, "fim": 141, "lado": "impar"}

        ]
    },
    "micro_05_equipe_320": {
        "profissionais": ["Acs - Kleber", "médico - Ewaldo", "enfª Adriana catunda."],
        "enderecos": [
            {"rua": "rua joaquim leitao", "inicio": 962, "fim": 1088, "lado": "par"},
            {"rua": "rua professor joaquim nogueira",
                "inicio": 900, "fim": 926, "lado": "par"},
            {"rua": "rua professor joaquim nogueira",
                "inicio": 931, "fim": 931, "lado": "todos"},
            {"rua": "rua hugo vitor", "inicio": 811, "fim": 970, "lado": "todos"},
            {"rua": "rua 1 monsenhor tabosa",
                "inicio": 16, "fim": 60, "lado": "todos"},
            {"rua": "rua 2 monsenhor tabosa",
                "inicio": 3, "fim": 53, "lado": "todos"},
            {"rua": "rua padre perdigao sampaio",
                "inicio": 1123, "fim": 1123, "lado": "par"},
            {"rua": "rua doutor manoel soares",
                "inicio": 41, "fim": 1041, "lado": "todos"},
            {"rua": "rua padre jose arteiro",
                "inicio": 359, "fim": 693, "lado": "impar"},
            {"rua": "rua tomas rodrigues", "inicio": 1432,
                "fim": 1458, "lado": "todos"}

        ]
    },
    "micro_01_equipe_320": {
        "profissionais": ["Acs - Eliana", "médico - Ewaldo", "enfª Adriana catunda."],
        "enderecos": [
            {"rua": "rua coronel joaquim franklim",
                "inicio": 665, "fim": 753, "lado": "impar"},
            {"rua": "rua coronel joaquim franklim",
                "inicio": 754, "fim": 785, "lado": "todos"},
            {"rua": "rua pedro melo", "inicio": 834, "fim": 1027, "lado": "todos"},
            {"rua": "rua padre perdigao sampaio",
                "inicio": 661, "fim": 839, "lado": "par"},
            {"rua": "rua jose leite gondim", "inicio": 1105,
                "fim": 1123, "lado": "impar"},
            {"rua": "rua joaquim leita", "inicio": 592, "fim": 760, "lado": "par"},
            {"rua": "rua tenente queiros", "inicio": 564, "fim": 856, "lado": "par"},
            {"rua": "rua tomas rodrigues", "inicio": 612,
                "fim": 1301, "lado": "todos"},
            {"rua": "rua tomas rodrigues", "inicio": 1307,
                "fim": 2207, "lado": "todos"}

        ]
    },
    "micro_09_equipe_320": {
        "profissionais": ["Acs - Michelly", "médico - Ewaldo", "enfª Adriana catunda."],
        "enderecos": [
            {"rua": "rua pedro melo", "inicio": 588, "fim": 680, "lado": "par"},
            {"rua": "rua professor joaquim nogueira",
                "inicio": 394, "fim": 838, "lado": "par"},
            {"rua": "rua tenente queiros", "inicio": 471,
                "fim": 497, "lado": "impar"},
            {"rua": "rua hugo vitor", "inicio": 503, "fim": 803, "lado": "impar"},
            {"rua": "rua doutor manoel soares",
                "inicio": 84, "fim": 154, "lado": "par"},
            {"rua": "rua padre jose arteiro",
                "inicio": 115, "fim": 209, "lado": "todos"},

        ]
    },
    "micro_04_equipe_320": {
        "profissionais": ["Acs - Regineide", "médico - Ewaldo", "enfª Adriana catunda."],
        "enderecos": [
            {"rua": "rua hugo vitor", "inicio": 496, "fim": 808, "lado": "par"},
            {"rua": "rua joaquim leitao", "inicio": 709,
                "fim": 911, "lado": "impar"},
            {"rua": "rua doutor manoel soares",
                "inicio": 160, "fim": 208, "lado": "par"},
            {"rua": "rua padre jose arteiro", "inicio": 232,
                "fim": 1421, "lado": "todos"},
            {"rua": "rua tomas rodrigues", "inicio": 820,
                "fim": 1403, "lado": "todos"},
            {"rua": "rua tenente queiros", "inicio": 447,
                "fim": 765, "lado": "todos"},
            {"rua": "rua pedro melo", "inicio": 703, "fim": 871, "lado": "todos"}

        ]
    }
}


def buscar_micro_por_enderecos(endereco_busca):
    endereco_busca = endereco_busca.lower().strip()
    partes = endereco_busca.split()
    try:
        numero = int(partes[-1])
        rua = " ".join(partes[:-1])
    except:
        return None, None  # Se não tiver número, já retorna

    for micro, dados in dados_ubs.items():
        for intervalo in dados["enderecos"]:
            if rua == intervalo["rua"]:
                if intervalo["inicio"] <= numero <= intervalo["fim"]:
                    return micro, dados["profissionais"]
    return None, None


# interface streamlit


st.set_page_config(page_title="Busca UAPS", layout="centered")
st.title("Espelho digital UAPS Meton de Alencar")

# input antes do botão
endereco = st.text_input("Digite o endereço:",placeholder="Ex.:rua do imperador 42")

# botão do contador
if 'contador_busca' not in st.session_state:
    st.session_state.contador_busca = 0
    if st.button("buscar"):
        if endereco:
            st.session_state.contador_busca += 1

        micro, profissionais = buscar_micro_por_enderecos(endereco)
        if micro:
            st.success(f"{micro}.")
            st.write("equipe:", ",".join(profissionais))
        else:
            st.error("endereço fora de cobertura do Meton de Alencar.")
    else:
        st.warning("digite o endeço")

# área do adm
senha_correta = "meton2026"
senha_digitada = st.sidebar.text_input("Adm", type="password")

if senha_digitada == senha_correta:
    st.sidebar.sucess("logado como Adm")
    st.sidebar.metric("total de buscas".st.session_state.contador_busca)
