import React, { useEffect, useState } from 'react'

const CreateCommentModal = (props) => {
    const [comment, setComment] = useState('')
    const toggleModal = (id) => {
      let modalroot = document.getElementById(`card${id}ModalRoot`)
      let body = document.querySelector('body')
      body.classList.toggle('no-scroll')
      modalroot.classList.toggle('d-none')
    }

    const modalClick = (e) => {
      e.preventDefault();
      e.stopPropagation();
    }

    const handleClick = (e) => {
        e.preventDefault()
        console.log("IT MADE IT HERE");
        props.createComment(props.id, comment)
        toggleModal(props.id)
    }

  return (
    <>  
        <div className='card'>
            <div
              onClick={() => toggleModal(props.id)}
            >
                <h5>Add Comment</h5>
            </div>
        </div>
    
        <div 
          className='modal-root d-none' 
          id={'card'+ props.id + 'ModalRoot'}
          onClick={() => toggleModal(props.id)}
        >
          <div 
            className='my-modal' 
            onClick={(e) => modalClick(e)}
          >
              <div className='modal-header'>
                  <p><b>{props.item.title}</b></p>
                  <button 
                    aria-label='close-modal'
                    onClick={() => toggleModal(props.id)}
                  >
                      X
                  </button>
              </div>

              <div className='modal-body'>
                    <textarea 
                        className='' 
                        value={comment}
                        onChange={(e)=> setComment(e.target.value)}
                    >

                    </textarea>
              </div>

              <div className='modal-footer'>
                <button 
                    className='modal-submit-btn' 
                    onClick={(e) => handleClick(e)}
                >Create</button>
              </div>
          </div>

        </div>
    </>
    
  )
}

export default CreateCommentModal