import os
import ast
import time
from flask import jsonify
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.document_loaders import SeleniumURLLoader

class RelatedLinksRepository:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="openai/gpt-4o-mini",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base=os.getenv("OPENROUTER_BASE_URL"),
        )

    def rate_site_relevance(self, site_url: str, user_resume: str):
        loader = SeleniumURLLoader(urls=[site_url], headless=True)
        try:
            docs = loader.load()
            if docs and len(docs) > 0:
                site_content = docs[0].page_content[:2000]
            else:
                return {"nota": 0, "explicacao": "Não foi possível carregar o conteúdo do site."}
        except Exception as e:
            return {"nota": 0, "explicacao": f"{str(e)}"}
        
        prompt = PromptTemplate(
            template=(
                "Resumo do usuário:\n{user_resume}\n\n"
                "Conteúdo do site:\n{site_content}\n\n"
                "Com base no resumo do usuário acima, dê uma nota de 0 a 100 para quão relevante este site é para o usuário, "
                "considerando interesses, perfil e contexto. Seja objetivo e explique brevemente o motivo da nota. "
                "Não de notas quebradas, apenas inteiras. "
                "A nota deve ser um número inteiro entre 0 e 100. "
                "Comente o porquê da nota dada, considerando o conteúdo do site e o resumo do usuário. "
                "Não de respostas genéricas, e nem baseadas em suposições. "
                "A resposta deve ser em português. "
                "Faça a resposta como uma análise do conteúdo do site, sem considerar aspectos técnicos como cookies, javascript, e etc. "
                "Formato da resposta: {{'nota': <nota>, 'explicacao': '<explicacao>'}}"
            ),
            input_variables=["user_resume", "site_content"]
        )

        chain = LLMChain(prompt=prompt, llm=self.llm)
        output = chain.run({"user_resume": user_resume, "site_content": site_content})

        try:
            output_dict = ast.literal_eval(output)
        except Exception as e:
            output_dict = {
                "nota": 0,
                "explicacao": f"Erro ao processar a resposta: {str(e)}"
            }

        return output_dict
