import './Meme.css'

function Meme({url}) {
    return (
        <div className="col meme-wrapper p-0 py-3">
            <img className="meme" src={url} />
        </div>
    )
}

export default Meme;