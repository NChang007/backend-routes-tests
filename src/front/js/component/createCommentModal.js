import React, { useEffect, useState } from 'react'

const CreateCommentModal = (props) => {
    const [comment, setComment] = useState('')
    // console.log("check12",props.item);
    const toggleModal = (id) => {
      let modalroot = document.getElementById(`card${id}ModalRoot`)
      let body = document.querySelector('body')
      body.classList.toggle('no-scroll')
      modalroot.classList.toggle('my-d-none')
    }
    const modalClick = (e) => {
      e.preventDefault();
      e.stopPropagation();
    }
    const handleClick = (e) => {
        e.preventDefault()
        // console.log("IT MADE IT HERE");
        props.createComment(props.discussionId, comment)
        toggleModal(props.id)
    }
    const handleClick2 = (e) => {
        e.preventDefault()
        // console.log("IT MADE IT HERE");
        props.createSubComment(props.discussionId, comment, props.item.id)
        toggleModal(props.id)
    }
    let isReply = false
    if(props.for === 'REPLY'){
      isReply = true
    }
    
  return (
    <>  
        <div className='card' onClick={() => toggleModal(props.id)} >
            <h5>{props.for}</h5>
        </div>
    
        <div 
          className='modal-root my-d-none' 
          id={'card'+ props.id + 'ModalRoot'}
          onClick={() => toggleModal(props.id)}
        >
          <div className='my-modal' onClick={(e) => modalClick(e)} >
              <div className='modal-header'>
                <p><b>{!isReply ? "comment on " + props.item.title :"Reply to " + props.item.comment}</b></p>
                <button aria-label='close-modal' onClick={() => toggleModal(props.id)} > X </button>
              </div>

              <div className='modal-body'>
                    <textarea 
                        className='' 
                        value={comment}
                        onChange={(e)=> setComment(e.target.value)}
                    ></textarea>
              </div>

              <div className='modal-footer'>
                {!isReply ? (
                  <button 
                      className='modal-submit-btn' 
                      onClick={(e) => handleClick(e)}
                  >Create</button>
                ):(
                  <button 
                      className='modal-submit-btn' 
                      onClick={(e) => handleClick2(e)}
                  >Reply</button>
                )
                }
              </div>
          </div>

        </div>
    </>
    
  )
}

export default CreateCommentModal