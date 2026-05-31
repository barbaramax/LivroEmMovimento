import { Link } from 'react-router-dom'

export default function HelpSection() {
  return (
    <section className="py-24 px-10 text-center bg-white">

      <h2 className="font-[Gloock] text-5xl font-bold mb-6">
        Como você pode ajudar
      </h2>

      <p className="text-gray-600 mb-16">
        Existem diversas formas de contribuir com nossa missão de levar conhecimento a todos.
      </p>

      <div className="grid md:grid-cols-3 gap-8">

   
        <div className="rounded-xl p-6 text-left shadow-sm bg-white hover:shadow-md transition">

          <h3 className="font-[Gloock] text-2xl font-semibold mb-4">
            Faça uma doação
          </h3>

          <p className="text-[#000000] mb-6">
            Sua doação transforma vidas. Doe livros ou valores para ajudar o projeto.
          </p>

          <Link
            to="/contato"
            className="text-[#1B56AE] font-medium hover:text-blue-600 transition"
          >
            Saiba mais
          </Link>

        </div>

        <div className="rounded-xl p-6 text-left shadow-sm bg-white hover:shadow-md transition">

          <h3 className="font-[Gloock] text-2xl font-semibold mb-4">
            Seja voluntário
          </h3>

          <p className="text-[#000000] mb-6">
            Junte-se a nós e transforme vidas participando de nossas ações.
          </p>

          <Link
            to="/voluntarios"
            className="text-[#1B56AE] font-medium hover:text-blue-600 transition"
          >
            Saiba mais
          </Link>

        </div>

      
        <div className="rounded-xl p-6 text-left shadow-sm bg-white hover:shadow-md transition">

          <h3 className="font-[Gloock] text-2xl font-semibold mb-4">
            Conheça nosso trabalho
          </h3>

          <p className="text-[#000000] mb-6">
            Siga nossas redes sociais e entre em contato para nos acompanhar.
          </p>

          <Link
            to="/sobre"
            className="text-[#1B56AE] font-medium hover:text-blue-600 transition"
          >
            Saiba mais
          </Link>

        </div>

      </div>

    </section>
  )
}