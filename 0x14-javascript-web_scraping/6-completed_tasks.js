#!/usr/bin/node
// script that creates an object with userid:total_no_of_tasks_done

const request = require('request');
const url = process.argv[2];

const fetchMovies = () => {
  const usersCompletedTasks = {};
  let completedTasks = 0;
  const uniqueId = [];
  const uniqueSet = new Set();
  request(url, { json: true }, (error, response, body) => {
    if (error) console.log(error);

    const result = body;
    for (const obj of result) {
      // filter userid to get unique userId
      if (!uniqueSet.has(obj.userId)) {
        uniqueSet.add(obj.userId);
        uniqueId.push(obj.userId);
      }
    }

    // nested loop comparing unique id in user obj
    // if true, count where completed==true
    for (const id of uniqueId) {
      completedTasks = 0;
      for (const obj of result) {
        if (+(obj.userId) === +(id) && obj.completed === true) {
          completedTasks++;
        }
      }
      usersCompletedTasks[id] = completedTasks;
    }
    console.log(usersCompletedTasks);
  });
};

fetchMovies();
