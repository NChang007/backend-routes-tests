import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import CreateCommentModal from "../component/createCommentModal";

export const Single = props => {
	const { store, actions } = useContext(Context);
	const [discussion, setDiscussion] = useState(false)
	const params = useParams();
	console.log(discussion);

	useEffect(async () => {
		try {
			const res = await fetch(store.backurl + "/api/discussions/"+ params.id);
			const data = await res.json();
				setDiscussion(data)
		} catch (error) {console.error(error)}
	},[])
	
	const createComment = async (discussion_id, comment) => {
		console.log("MADE IT TO THIS SHIT");
		const opts = {
			method: "POST",
			mode: "cors",
			headers: {
			  "Content-Type": "application/json",
			  "Access-Control-Allow-Origin": "*",
			},
			body: JSON.stringify({
                discussion_id: discussion_id,
                comment: comment,
			}),
		};
		try {
			const res = await fetch(store.backurl + "/api/comment", opts);
			const data = await res.json();
				setDiscussion(data)

		} catch (error) {console.error(error)}
	}

	return (
		discussion &&
		<div className="discussion-info">
			<div className="header">
				<p>created by: {discussion.createdBy.name}</p>
				<p>title:{discussion.title}</p>
			</div>
			<div>
				<p>discussion promt: {discussion.discussion}</p>
			</div>
			<div>
				comment section
				{
					discussion.comments.map((item,idx)=>{
						console.log("COMMENTS", item);
						return (
							<div>
								<div key={idx} className="dicussion-comment">
									<p>{item.created_by.name}</p>
									<p>{item.comment}</p>
								</div>
								{
									item.children.map((item, idx)=> {
										return (
											<div key={idx} className="dicussion-sub-comment">
												<p>{item.created_by.name}</p>
												<p>{item.comment}</p>
											</div>
										)
									})
								}
							</div>
						)
					})
				}
			</div>
			<CreateCommentModal id={params.id} item={discussion} createComment={createComment} />
		</div>
	);
};

Single.propTypes = {
	match: PropTypes.object
};
