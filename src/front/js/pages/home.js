import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Link } from "react-router-dom";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<h2>Discussions</h2>
			<div className="discussion-card-container">
				{
					store.discussions.map((item,idx) => {
						return (
							<div className="discussion-card" key={idx}>
								<p>{item.createdBy.name}</p>
								<Link to={"/discussion/"+ item.id}><p>{item.title}</p></Link>
							</div>
						)
					})
				}
			</div>
		</div>
	);
};
