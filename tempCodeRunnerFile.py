rounded_results = np.round(pose_results[0].keypoints.numpy(), 1)

        try:
            # Get the keypoints for the body parts
            left_wrist = rounded_results[0][self.body_index["left_wrist"]]
            right_wrist = rounded_results[0][self.body_index["right_wrist"]]
        except:
            print("No human detected.")
            return pose_annotated_frame, False