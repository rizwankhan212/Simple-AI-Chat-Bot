import { useState } from "react"
import axios from "axios"
import ReactMarkdown from "react-markdown";
import "./App.css"
function App() {
  const [prompt,setPrompt] = useState("")
  const [response,setResponse] = useState("")
  const [loading,setLoading] = useState(false)

  const handleChange = (event)=>{
    setPrompt(event.target.value)
  }
  const handleGenerate = async (event)=>{
      setLoading(true)
      const res = await axios.post("http://127.0.0.1:8000/generate",
        {
            prompt:prompt
        }
      )
      setResponse(res.data.response)
      setLoading(false)
  }
  return (
    <>
      <div className="container">
      <h1>Full stack AI inegration app</h1>
      <textarea
  value={prompt}
  onChange={handleChange}
  placeholder="Ask me anything..."
></textarea>

<button onClick={handleGenerate}>
 { loading ? "Generating ...":"🚀 Generate Response"}
</button>
      <div className="response-box">
          <h2>AI Response</h2>
          <ReactMarkdown>{response}</ReactMarkdown>
      </div>
      </div>
    </>
  )
}

export default App
